import random
import os
import feedparser
import dotenv
import subprocess

from apscheduler.schedulers.blocking import BlockingScheduler
from infra import twitter, rss
from tasks import task1_note_tweet

dotenv.load_dotenv()
API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')
RSS_URL = os.getenv('BLOG_RSS_URL')

scheduler = BlockingScheduler()
twitter_client = twitter.get_client(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
feed = rss.get_feed(RSS_URL).entries

@scheduler.scheduled_job('interval', minutes=30)
def job_30_minutes():
    feed_entry = random.choice(feed)
    task1_note_tweet.tweet_note(twitter_client.update_status, feed_entry.title, feed_entry.links[0].href)

scheduler.start()
