import configparser
import os
import sys

import twitter

config = configparser.ConfigParser()
ROOT_DIR = os.path.dirname(sys.modules['__main__'].__file__)
print(ROOT_DIR)

config.read(os.path.join(ROOT_DIR, 'rapbot.conf'))


api = twitter.Api(
	consumer_key=config['twitter']['consumer_key'],
	consumer_secret=config['twitter']['consumer_secret'],
	access_token_key=config['twitter']['access_token_key'],
    access_token_secret=config['twitter']['access_token_secret'])


def get_latest_status(username):
	statuses = api.GetUserTimeline(screen_name=username)
	return [s.text for s in statuses]