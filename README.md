<div align="center">

<img src="https://raw.githubusercontent.com/Studio1HQ/Studio1HQ/main/assets/banners/pipecat-bright-data.webp" alt="TechStack Hotline with Pipecat and Bright Data: A voice assistant that reads you live tech news" width="100%" />

<br />
<br />

# TechStack Hotline with Pipecat and Bright Data

### A voice assistant that reads you live tech news

A Pipecat voice bot over Daily WebRTC that uses GPT-4o-mini, ElevenLabs speech and Bright Data calls to search Google News and read article text on request.

<br />

[![Built by Studio1](https://img.shields.io/badge/Built_by_Studio1-f97316?style=for-the-badge&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNjAgMTYwIiBmaWxsPSJub25lIj48cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTAgMzVDMCAxNi42ODA3IDE0LjA3NDQgMS42NDg0NCAzMiAwLjEyNjk1M1YxNDFINTEuMDUyM0M1Mi40MzA4IDEzNy4zNDQgNTQuNzQ0NiAxMzMuNjg5IDU3Ljk5MzggMTMwLjAzM0M2MS4xNDQ2IDEyNi41MDggNjQuNjg5MiAxMjMuNDQgNjguNjI3NyAxMjAuODI5QzcyLjU2NjIgMTE4LjM0OSA3Ni4zNTY5IDExNi43ODIgODAgMTE2LjEyOVY4Ni43NTQ0Qzc1LjQ3MDggODcuOTI5MiA3MS4zODQ2IDg5LjY5MTkgNjcuNzQxNSA5Mi4wNDE1QzY0IDk0LjUyMjUgNjAuNzUwOCA5Ny40NiA1Ny45OTM4IDEwMC44NTRDNTYuNTM0NSAxMDIuNzIgNTUuMjU0NSAxMDQuNjU5IDU0LjE1MzkgMTA2LjY3MVYwSDEyNUMxNDQuMzMgMCAxNjAgMTUuNjY5OSAxNjAgMzVWMTI1QzE2MCAxNDQuMzMgMTQ0LjMzIDE2MCAxMjUgMTYwSDEyNFYxOEgxMDQuOTQ4QzEwMy41NjkgMjEuNjgxNiAxMDEuMjU1IDI1LjM2MjggOTguMDA2MiAyOS4wNDQ0Qzk0Ljg1NTQgMzIuNTk0MiA5MS4zMTA4IDM1LjY4NDEgODcuMzcyMyAzOC4zMTRDODMuNDMzOCA0MC44MTIgNzkuNjQzMSA0Mi4zODk2IDc2IDQzLjA0NzRWNzIuNjMwNEM4MC41MjkyIDcxLjQ0NzMgODQuNjE1NCA2OS42NzI0IDg4LjI1ODUgNjcuMzA1N0M5MiA2NC44MDc2IDk1LjI0OTIgNjEuODQ5MSA5OC4wMDYyIDU4LjQzMDdDOTkuNDY1NSA1Ni41NTEzIDEwMC43NDUgNTQuNTk4NiAxMDEuODQ2IDUyLjU3MjNWMTYwSDM1QzE1LjY3IDE2MCAwIDE0NC4zMyAwIDEyNVYzNVoiIGZpbGw9IiNmZmZmZmYiLz48L3N2Zz4K)](https://studio1hq.com)
[![Built with Bright Data](https://img.shields.io/badge/Built_with_Bright_Data-141414?style=for-the-badge)](https://brightdata.com)

[Bright Data docs](https://docs.brightdata.com) &nbsp;·&nbsp; [Bright Data](https://brightdata.com) &nbsp;·&nbsp; [Pipecat](https://pipecat.ai) &nbsp;·&nbsp; [More examples](https://github.com/Studio1HQ) &nbsp;·&nbsp; [studio1hq.com](https://studio1hq.com)

</div>

<br />

## Overview

TechStack Hotline is a voice assistant for developers. You talk to it, ask about a technology, and it reads back recent news. The pipeline runs on [Pipecat](https://pipecat.ai) with Daily WebRTC for audio, GPT-4o-mini for the conversation, and ElevenLabs for speech.

Bright Data supplies the news data. `bright_data.py` posts to the Bright Data `dca/trigger` endpoint with a `news` zone to search Google News, and with an `unblocker` zone to fetch article text. The LLM calls these through two tools: `get_tech_news` and `read_article`.

## Features

- **Voice-activated news**: Ask about any technology and get the latest stories.
- **Article summaries**: Returns up to five articles with title, source, URL and snippet.
- **Full article reading**: Fetches article text (first 4,000 characters) on request.
- **Natural conversation**: Silero voice activity detection, OpenAI function calling and ElevenLabs speech.
- **Extensible tools**: Add new LLM tools in `tools.py`.

## Tech stack

| Layer | Tool |
| --- | --- |
| Voice framework | [Pipecat](https://pipecat.ai) |
| Transport | [Daily](https://www.daily.co) WebRTC |
| Web data | [Bright Data](https://brightdata.com) |
| LLM | [OpenAI](https://platform.openai.com) GPT-4o-mini |
| Speech | [ElevenLabs](https://elevenlabs.io) TTS, Silero VAD |

## Getting started

### Prerequisites

- Python 3.10+
- A [Bright Data](https://brightdata.com) API key with news and unblocker zones
- An OpenAI API key
- An ElevenLabs API key
- A Daily account and API key

### Installation

```bash
git clone https://github.com/Studio1HQ/pipecat-bright-data.git
cd pipecat-bright-data
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -e .
cp env.example .env
```

### Environment variables

| Variable | Description |
| --- | --- |
| `BRIGHT_DATA_API_KEY` | Bright Data API key. |
| `OPENAI_API_KEY` | OpenAI key for GPT-4o-mini. |
| `ELEVENLABS_API_KEY` | ElevenLabs key for text to speech. |
| `DAILY_API_KEY` | Daily key for rooms and transport. |

`env.example` in the repo is empty, so create `.env` with these variables.

### Run

```bash
python -m techstack_hotline.bot
```

The README refers to `techstack_hotline.main`, but the entry point in the repo is `bot.py`, which uses the Pipecat runner. Join the Daily room URL in a browser, or use a phone number if you configured one in Daily, then say something like "Hi, what's new with Python?"

## How it works

```text
User -> Daily transport (WebRTC) -> voice input -> OpenAI LLM -> Bright Data -> news processing -> voice response
```

```text
src/techstack_hotline/
├── bot.py          # Pipecat pipeline and Daily transport
├── bright_data.py  # search_tech_news, scrape_article
├── tools.py        # get_tech_news, read_article tool functions
└── assets/robot01.jpeg
```

The pipeline is `transport.input()`, user aggregator, LLM, TTS, `transport.output()`, assistant aggregator. To change the voice, set a different `voice_id` on `ElevenLabsTTSService`. To add a tool, write an async function in `tools.py` and register it with the LLM.

## Resources

- [Bright Data docs](https://docs.brightdata.com): Web data and API documentation.
- [Bright Data](https://brightdata.com): Account and API key.
- [Pipecat docs](https://docs.pipecat.ai): Pipelines, services and runners.

<br />

---

<div align="center">

<a href="https://studio1hq.com">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Studio1HQ/website/main/brand/studio1-logo-on-dark.svg" />
    <img src="https://raw.githubusercontent.com/Studio1HQ/website/main/brand/studio1-logo-on-light.svg" alt="Studio1" width="160" />
  </picture>
</a>

Built by **[Studio1](https://studio1hq.com)**, the technical content and DevRel partner for devtool teams. Made with [Bright Data](https://brightdata.com).<br />
Browse more open-source examples at [github.com/Studio1HQ](https://github.com/Studio1HQ).

[![Website](https://img.shields.io/badge/studio1hq.com-0b0807?style=for-the-badge&logo=googlechrome&logoColor=white)](https://studio1hq.com)
[![Book a call](https://img.shields.io/badge/Book_a_strategy_call-f97316?style=for-the-badge&logo=googlecalendar&logoColor=white)](https://cal.com/studio1/collab)
[![X](https://img.shields.io/badge/%40Studio1HQ-141414?style=for-the-badge&logo=x&logoColor=white)](https://x.com/Studio1HQ)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0a66c2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/company/studio1hq/)

<sub><a href="https://studio1hq.com">studio1hq.com</a> · Technical content, docs, video and DevRel for devtools</sub>

</div>
