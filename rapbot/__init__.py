
# start
## 1) start twitter listening interface
## 2) when new tweet, process()
## 3) process_tweet()
## 3a) parse and strip tweets of links
## 4) update database with tweet
## 5) convert tweet to something rapable ?????
## 6) rap it (play)

import glob
import hashlib
import os

from rapbot.twitterapi import get_latest_status
from rapbot.speech import rap



def store_tweet(tweet, tweet_dir):
    if not os.path.exists(tweet_dir):
        os.makedirs(tweet_dir)

    tweet_hash = hashlib.md5(tweet.encode('utf-8')).hexdigest()
    tweet_file = os.path.join(tweet_dir, tweet_hash)

    with open(tweet_file, 'w') as f:
        f.write(tweet)
        f.close()

def main():
    tweet_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'tweets')

    try:
        tweet = get_latest_status('realdonaldtrump')[0]
        store_tweet(tweet, tweet_dir)
    except Exception as e:
        cached_tweets = glob.glob(os.path.join(tweet_dir, '*'))
        latest_tweet = max(cached_tweets, key=os.path.getctime)
        with open(latest_tweet, 'r') as f:
            tweet = f.read()
    rap(tweet)