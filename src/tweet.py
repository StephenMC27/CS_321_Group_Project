class Tweet:

    def __init__(self, weather_str: str, song_str: str, quote_str: str, image):
        self.weather_str = weather_str
        self.song_str = song_str
        self.quote_str = quote_str
        self.image = image

    def format(self) -> str:
        tweet_str = 'Good Morning, GMU!\n'
        tweet_str += f'Current weather in Fairfax: {self.weather_str}\n'
        tweet_str += f'Listen to this: {self.song_str}\n'
        tweet_str += quoute_str
