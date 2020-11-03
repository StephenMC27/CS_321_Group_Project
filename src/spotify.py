import spotipy
import yaml
from random import randint
from spotipy.oauth2 import SpotifyClientCredentials

class Spotify:

    weeklySongs = []

    @classmethod
    def fetch_songs(cls):
        #read in API keys from config.yaml
        with open('../config/config.yaml', 'r') as config_file:
	        config = yaml.load(config_file, Loader=yaml.FullLoader)
            
        #save API keys for spotify API
        SPOTIFY_CLIENT_ID = config['spotify']['client_id']
        SPOTIFY_CLIENT_SECRET = config['spotify']['client_secret']
        
        sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET))
        
        # generate random value for offset to provide random selection
        rand_Offset = randint(0,80)
        
        # call to grab items from weekly new release playlist, with random offset
        result1 = sp.playlist_items(playlist_id='37i9dQZF1DX4JAvHpjipBk', offset=rand_Offset, limit=7, additional_types={'track'})

        # print track url for each track desired
        for idx, track in enumerate(result1['items']):
            trackInfo = track['track']
            cls.weeklySongs.append(trackInfo['external_urls']['spotify'])

    @classmethod
    def get_song(cls, day):
        return(cls.weeklySongs[day])


"""
# call to grab items from weekly new release playlist, with random offset
result1 = sp.playlist_items(playlist_id='37i9dQZF1DX4JAvHpjipBk', offset=rand_Offset, limit=7, additional_types={'track'})

# print track url for each track desired
for idx, track in enumerate(result1['items']):
	trackInfo = track['track']
	# info: trackInfo['name']
	# track id: trackInfo['id']
	# spotify external url: trackInfo['external_urls']['spotify']
	print(rand_Offset+idx, " spotify url: " + trackInfo['external_urls']['spotify'])
"""
