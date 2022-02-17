import feedparser

def get_feed(url: str) -> object:
    return feedparser.parse(url)