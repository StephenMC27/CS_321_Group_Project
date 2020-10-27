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

#api.update_status('Testing, testing, 1, 2, 3...')
