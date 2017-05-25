
# start
## 1) start twitter listening interface
## 2) when new tweet, process()
## 3) process_tweet()
## 3a) parse and strip tweets of links
## 4) update database with tweet
## 5) convert tweet to something rapable ?????
## 6) rap it (play)

from rapbot.twitterapi import get_latest_status

def main():
    print(get_latest_status('realdonaldtrump')[0])
