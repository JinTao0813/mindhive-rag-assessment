import os
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

OUTLETS_URL = "https://zuscoffee.com/category/store/kuala-lumpur-selangor/"

def scrape_outlets():
    response = requests.get(OUTLETS_URL)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, "html.parser")

    outlets = []

    # Each outlet is one <article> card
    outlet_cards = soup.select("article.elementor-post")

    for card in outlet_cards:

        # 1. Outlet Name (first <p> with elementor-heading-title)
        title_tag = card.select_one("p.elementor-heading-title")
        title = title_tag.get_text(strip=True) if title_tag else None

        # 2. Location Category (KL/Selangor)
        category_tag = card.select_one("h2.elementor-heading-title a")
        category = category_tag.get_text(strip=True) if category_tag else None

        # 3. Address (second <p> in article)
        p_tags = card.select("p")
        address = p_tags[1].get_text(strip=True) if len(p_tags) > 1 else None

        # 4. Google Maps Link
        direction_tag = card.select_one("a.premium-button")
        maps_url = direction_tag["href"] if direction_tag else None

        outlets.append({
            "name": title,
            "category": category,
            "address": address,
            "maps_url": maps_url
        })

    # Save data
    os.makedirs("data", exist_ok=True)

    with open("data/outlets.json", "w", encoding="utf-8") as f:
        json.dump(outlets, f, indent=4, ensure_ascii=False)

    df = pd.DataFrame(outlets)
    df.to_csv("data/outlets.csv", index=False)

    print(f"Scraped {len(outlets)} outlets successfully!")

if __name__ == "__main__":
    scrape_outlets()
