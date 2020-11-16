import tweepy

auth = None
api = None

#connect bot to Twitter's API
def authorize(consumer_key, consumer_secret, access_key, access_secret):
    global auth
    global api
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret) #established bot's access to Twitter API
        auth.set_access_token(access_key, access_secret) #associate bot with specific twitter account
        api = tweepy.API(auth) #object for making API requests
        print('Successfully connected to Twitter API!')
    except:
        print('Error: Twitter API access could not be established.')

#publish Tweet
def publish_tweet(tweet):
    global auth
    global api
    try:
    # tweet with formatted string and today's image media
        media = api.media_upload(tweet.image_path)
        tweet_str = tweet.format()
        api.update_status(status=tweet_str, media_ids=[media.media_id])
        print('Tweet successfully published!')
    except Exception as e:
        print(e)
        # print('Error: Twitter API access has not been established.')