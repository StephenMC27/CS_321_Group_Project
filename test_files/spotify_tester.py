#Spotify tester file

import spotipy
import yaml
from random import randint
from spotipy.oauth2 import SpotifyClientCredentials

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
    print("name: " + trackInfo['name'])
    print("track id: " + trackInfo['id'])
    print("spotify url: " + trackInfo['external_urls']['spotify'])
    print()
