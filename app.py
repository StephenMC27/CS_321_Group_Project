import tweepy

#API credentials for application
CONSUMER_KEY = 'FLIiklJ1Ju7WiS5FmzAqtytNZ'
CONSUMER_SECRET = 'ZD6jyBaH0BvqdnnKwu1ssrnEwAwOcNFxcGGLEXC9jCDv4I209Z'

#API credentials for associating application with @GoodMorningGMU account
ACCESS_KEY = '1310571338936049664-G76N1UbCtuLbn20tvGjjOos8GiDy8f'
ACCESS_SECRET = 'bYq5eHFZ2MdiKo4Cq5qXeDNFfmZCaCP7I7zCjSNTMPEip'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)

#api.update_status('Testing, testing, 1, 2, 3...')