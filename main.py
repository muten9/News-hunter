import os
import feedparser
import requests

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

RSS_FEEDS = [
    "https://www.globenewswire.com/RssFeed/orgclass/1/feedTitle/GlobeNewswire%20-%20News%20about%20Public%20Companies",
]

KEYWORDS = [
    "merger",
    "acquisition",
    "fda",
    "contract",
    "phase 3",
    "phase 2",
    "nasa",
]
def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    requests.post(
        url,
        data={
            "chat_id": CHAT_ID,
            "text": text
        },
        timeout=30
    )


def scan():
    for feed in RSS_FEEDS:

        news = feedparser.parse(feed)

        for item in news.entries[:10]:

            title = item.title
            low = title.lower()

            for word in KEYWORDS:

                if word in low:

                    send_message(
                        f"🚨 {title}\n\n{item.link}"
                    )

                    break


if __name__ == "__main__":
    scan()
