import tweepy
import yaml

#read in API keys from config.yaml
with open('config.yaml', r) as config_file:
    config = yaml.load(config_file)

#save API keys
CONSUMER_KEY = config['twitter']['consumer_key']
CONSUMER_SECRET = config['twitter']['consumer_secret']
ACCESS_KEY = config['twitter']['access_key']
ACCESS_SECRET = config['twitter']['access_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET) #established bot's access to Twitter API
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET) #associates bot with specific Twitter account

api = tweepy.API(auth) #object for making API requests

#api.update_status('Testing, testing, 1, 2, 3...')
