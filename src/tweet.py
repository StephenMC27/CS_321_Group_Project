class Tweet:

    def __init__(self, weather_str: str, song_str: str, quote_str: str): #needs to include image in final version
        self.weather_str = weather_str
        self.song_str = song_str
        self.quote_str = quote_str
        self.image = None

    def format(self) -> str:
        tweet_str = 'Good Morning, GMU!\n\n'
        tweet_str += f'Current weather in Fairfax: {self.weather_str}\n\n'
        tweet_str += f'Listen to this: {self.song_str}\n\n'
        tweet_str += self.quote_str
        return tweet_str
