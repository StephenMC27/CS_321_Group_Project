import tweepy

class Bot:

    auth = None
    api = None

    #connect bot to Twitter's API
    def authorize(cls, consumer_key, consumer_secret, access_key, access_secret):
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET) #established bot's access to Twitter API
        auth.set_access_token(ACCESS_KEY, ACCESS_SECRET) #associate bot with specific Twitter account

    #publish Tweet
    def publish_tweet(cls, tweet_str):
        api = tweepy.API(auth) #object for making API requests
        api.update_status(tweet_str)
