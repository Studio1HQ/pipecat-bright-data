import os
import json
from dotenv import load_dotenv
from loguru import logger
from PIL import Image

from pipecat.audio.vad.silero import SileroVADAnalyzer
from pipecat.frames.frames import (
    BotStartedSpeakingFrame,
    BotStoppedSpeakingFrame,
    Frame,
    LLMRunFrame,
    OutputImageRawFrame,
    SpriteFrame,
)
from pipecat.pipeline.pipeline import Pipeline
from pipecat.pipeline.runner import PipelineRunner
from pipecat.pipeline.task import PipelineParams, PipelineTask
from pipecat.processors.aggregators.llm_context import LLMContext
from pipecat.processors.aggregators.llm_response_universal import (
    LLMContextAggregatorPair,
)
from pipecat.processors.frame_processor import FrameDirection, FrameProcessor
from pipecat.processors.frameworks.rtvi import RTVIConfig, RTVIObserver, RTVIProcessor
from pipecat.runner.types import RunnerArguments
from pipecat.services.elevenlabs.tts import ElevenLabsTTSService
from pipecat.services.openai.llm import OpenAILLMService
from pipecat.transports.base_transport import BaseTransport
from pipecat.transports.daily.transport import DailyParams, DailyTransport

from techstack_hotline.tools import (
    get_tech_news,
    read_article,
)

load_dotenv(override=True)


script_dir = os.path.dirname(__file__)
robot_path = os.path.join(script_dir, "assets/robot01.jpeg")

with Image.open(robot_path) as img:
    quiet_frame = OutputImageRawFrame(
        image=img.tobytes(),
        size=img.size,
        format=img.format,
    )
talking_frame = quiet_frame

class TalkingAnimation(FrameProcessor):
    def __init__(self):
        super().__init__()
        self._talking = False

    async def process_frame(self, frame: Frame, direction: FrameDirection):
        await super().process_frame(frame, direction)

        if isinstance(frame, BotStartedSpeakingFrame) and not self._talking:
            await self.push_frame(talking_frame)
            self._talking = True

        if isinstance(frame, BotStoppedSpeakingFrame):
            await self.push_frame(quiet_frame)
            self._talking = False

        await self.push_frame(frame, direction)

async def run_bot(transport: BaseTransport):
    tts = ElevenLabsTTSService(
        api_key=os.getenv("ELEVENLABS_API_KEY"),
        voice_id="pNInz6obpgDQGcFmaJgB",
    )

    llm = OpenAILLMService(
        api_key=os.getenv("OPENAI_API_KEY"),
        model="gpt-4o-mini",
        tools=[
            {
                "name": "get_tech_news",
                "description": "Get latest tech news",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "technology": {"type": "string"},
                    },
                    "required": ["technology"],
                },
                "handler": get_tech_news,
            },
            {
                "name": "read_article",
                "description": "Read full article from URL",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "url": {"type": "string"},
                    },
                    "required": ["url"],
                },
                "handler": read_article,
            },
        ],
    )

    messages = [
        {
            "role": "system",
            "content": (
                "You are TechStack Hotline, a live developer news assistant. "
                "You fetch real-time tech news using Bright Data. "
                "Ask the user what technology they want updates on."
            ),
        }
    ]

    context = LLMContext(messages)
    aggregator = LLMContextAggregatorPair(context)
    rtvi = RTVIProcessor(config=RTVIConfig(config=[]))
    ta = TalkingAnimation()

    pipeline = Pipeline(
        [
            transport.input(),
            rtvi,
            aggregator.user(),
            llm,
            tts,
            ta,
            transport.output(),
            aggregator.assistant(),
        ]
    )

    task = PipelineTask(
        pipeline,
        PipelineParams(enable_metrics=True),
        observers=[RTVIObserver(rtvi)],
    )

    await task.queue_frame(quiet_frame)

    @rtvi.event_handler("on_client_ready")
    async def ready(rtvi):
        await rtvi.set_bot_ready()
        await task.queue_frames([LLMRunFrame()])

    runner = PipelineRunner(handle_sigint=False)
    await runner.run(task)

async def bot(runner_args: RunnerArguments):
    transport = DailyTransport(
        runner_args.room_url,
        runner_args.token,
        "TechStack Hotline",
        DailyParams(
            audio_in_enabled=True,
            audio_out_enabled=True,
            video_out_enabled=True,
            vad_analyzer=SileroVADAnalyzer(),
            transcription_enabled=True,
        ),
    )

    await run_bot(transport)

if __name__ == "__main__":
    from pipecat.runner.run import main
    main()