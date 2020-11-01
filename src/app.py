import tweepy
import yaml
from tweet import Tweet
from bot import Bot

#read in API keys from config.yaml
with open('../config/config.yaml', 'r') as config_file:
    config = yaml.load(config_file, yaml.FullLoader)

#save API keys
CONSUMER_KEY = config['twitter']['consumer_key']
CONSUMER_SECRET = config['twitter']['consumer_secret']
ACCESS_KEY = config['twitter']['access_key']
ACCESS_SECRET = config['twitter']['access_secret']

#get weather stuff
#get song rec. stuff
quote = Quotes.get_quote()
#get image stuff
#create new Tweet instance with above info
#call Bot.publish_tweet(), passing in new tweet string

#test tweet
tweet = 'Testing, testing, 1, 2, 3...'
Bot.authorize(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
Bot.publish_tweet(tweet)
