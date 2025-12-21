from techstack_hotline.bright_data import (
    search_tech_news,
    scrape_article,
)

async def get_tech_news(technology: str):
    articles = await search_tech_news(technology)

    if not articles:
        return "No recent news found."

    response = f"Latest {technology} news:\n\n"
    for a in articles[:3]:
        response += (
            f"Title: {a['title']}\n"
            f"Source: {a['source']}\n"
            f"Summary: {a['snippet']}\n\n"
        )

    return response

async def read_article(url: str):
    content = await scrape_article(url)
    return content