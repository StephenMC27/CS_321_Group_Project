import spotipy
import yaml

#read in API keys from config.yaml
with open('config.yaml', 'r') as config_file:
    config = yaml.load(config_file)

#save API keys
SPOTIFY_CLIENT_ID = config['spotify']['client_id']
SPOTIFY_CLIENT_SECRET = config['spotify']['client_secret']

from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET))


"""
example usage of search feature for spotify api: 
results = sp.search(q='maren morris', limit=10)
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['name'])
"""

# call with a random value for offset to provide random selection from the weekly created playlist

result1 = sp.playlist_items(playlist_id='37i9dQZF1DX4JAvHpjipBk', offset=0, limit=7, additional_types={'track'})
print()
for idx1, track1 in enumerate(result1['items']):
	trackInfo = track1['track']
	# info: trackInfo['name']
	# track id: trackInfo['id']
	# spotify external url: trackInfo['external_urls']['spotify']
	print("spotify url: " + trackInfo['external_urls']['spotify'])
	print()
	
# maybe construct an array to store the songs for the week or something of that sort?



