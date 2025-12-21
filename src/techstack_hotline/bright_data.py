import os
import httpx

BRIGHT_DATA_API_KEY = os.getenv("BRIGHT_DATA_API_KEY")
BASE_URL = "https://api.brightdata.com/dca/trigger"

HEADERS = {
    "Authorization": f"Bearer {BRIGHT_DATA_API_KEY}",
    "Content-Type": "application/json",
}

async def search_tech_news(query: str):
    payload = {
        "zone": "news",
        "url": f"https://news.google.com/search?q={query}+technology",
        "format": "json",
    }
    
    async with httpx.AsyncClient(timeout=30) as client:
        r = await client.post(BASE_URL, headers=HEADERS, json=payload)
        r.raise_for_status()
        data = r.json()
    articles = []
    for item in data.get("articles", [])[:5]:
        articles.append(
            {
                "title": item.get("title", ""),
                "source": item.get("source", ""),
                "url": item.get("url", ""),
                "snippet": item.get("description", ""),
            }
        )

    return articles

async def scrape_article(url: str):
    payload = {
        "zone": "unblocker",
        "url": url,
        "format": "text",
    }
    async with httpx.AsyncClient(timeout=30) as client:
        r = await client.post(BASE_URL, headers=HEADERS, json=payload)
        r.raise_for_status()
        return r.text[:4000]