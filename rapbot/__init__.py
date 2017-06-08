
# start
## 1) start twitter listening interface
## 2) when new tweet, process()
## 3) process_tweet()
## 3a) parse and strip tweets of links
## 4) update database with tweet
## 5) convert tweet to something rapable ?????
## 6) rap it (play)

from rapbot.twitterapi import get_latest_status
from rapbot.speech import say

def main():
    tweet = get_latest_status('realdonaldtrump')[0]
    say(tweet)