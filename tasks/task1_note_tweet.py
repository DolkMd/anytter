from typing import Callable
from log.logger import logger

TWEET_BODY = """
{}
{}
#駆け出しエンジニア
#駆け出しエンジニアと繋がりたい
#プログラミング
#プログラミング初心者
#プログラミング初学者
#プログラミングできない
"""

def tweet_note(tweet : Callable[[str], None], title: str, url: str, retry=True):
    try:
        tweet(TWEET_BODY.format(title, url))
        logger.info("tweet: " + TWEET_BODY.format(title, url))
    except:
        if retry:
            logger.info("retry tweet_note")
            tweet_note(tweet, title, url, retry=False)
        else:
            logger.info("failed to tweet")