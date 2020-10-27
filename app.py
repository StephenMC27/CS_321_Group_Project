import tweepy
import yaml
from tweet import Tweet
from bot import Bot

#read in API keys from config.yaml
with open('config.yaml', r) as config_file:
    config = yaml.load(config_file)

#save API keys
CONSUMER_KEY = config['twitter']['consumer_key']
CONSUMER_SECRET = config['twitter']['consumer_secret']
ACCESS_KEY = config['twitter']['access_key']
ACCESS_SECRET = config['twitter']['access_secret']

#get weather stuff
#get song rec. stuff
#get quote stuff
#get image stuff
#create new Tweet instance with above info
#call Bot.publish_tweet(), passing in new tweet string
