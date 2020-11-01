import tweepy

class Bot:

    auth = None
    api = None

    #connect bot to Twitter's API
    @classmethod
    def authorize(cls, consumer_key, consumer_secret, access_key, access_secret):
        try:
            cls.auth = tweepy.OAuthHandler(consumer_key, consumer_secret) #established bot's access to Twitter API
            cls.auth.set_access_token(access_key, access_secret) #associate bot with specific twitter account
            cls.api = tweepy.API(cls.auth) #object for making API requests
            print('Successfully connected to Twitter API!')
        except:
            print('Error: Twitter API access could not be established.')

    #publish Tweet
    @classmethod
    def publish_tweet(cls, tweet_str):
        try:
            cls.api.update_status(tweet_str)
            print('Tweet successfully published!')
        except:
            print('Error: Twitter API access has not been established.')
