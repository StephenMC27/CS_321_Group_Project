import tweepy
import yaml
import schedule
import bot
import quotes
import weather
import photo
import spotify
import weather
from tweet import Tweet

MAX_TWEET_LENGTH = 280
PHOTO_PATH = '../imagecache/todayspic.jpg'

#read in API keys from config.yaml
with open('../config/config.yaml', 'r') as config_file:
    config = yaml.load(config_file, yaml.FullLoader)

#save Twitter API keys
CONSUMER_KEY = config['twitter']['consumer_key']
CONSUMER_SECRET = config['twitter']['consumer_secret']
ACCESS_KEY = config['twitter']['access_key']
ACCESS_SECRET = config['twitter']['access_secret']

def create_tweet(): #returns a Tweet object
    weather.gather_info()
    weather_str = weather.get_values(weather.j)
    spotify.fetch_songs() # want to change this to only do this once a week
    song_str = spotify.get_song(0) # instead of zero, pass in day of week
    quotes.fetch_quotes('../csv/quotes.csv')
    photo.fetch_photo() #fetches photo for tweet

    #loop to get quote that fits within Twitter's character limit
    while True:
        quote_str = quotes.get_quote()
        current_length = len(weather_str + '\n\n' + song_str + '\n\n' + quote_str)
        if current_length <= MAX_TWEET_LENGTH:
            break

    #get image stuff
    tweet = Tweet(weather_str, song_str, quote_str, PHOTO_PATH)
    return tweet

def run_bot():
    #call Bot.publish_tweet(), passing in new tweet string
    tweet = create_tweet()
    bot.authorize(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
    bot.publish_tweet(tweet)

schedule.every().day.at("08:05").do(run_bot)
run_bot() #test

# if __name__ == '__main__':
#     while True:
#         schedule.run_pending()
