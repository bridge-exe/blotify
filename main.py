import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth


client_id = 'ca352b7949dd41018f9fd85dc2aeb024'
secret = '17314964a6e14136b05c9bdbd9234ae1'

auth = SpotifyClientCredentials(client_id, secret)
sp = spotipy.Spotify(auth_manager=auth)

user_id = 's3haqvhbykrrknwz1c0wwukwn'
playlist_to_sort = 'Copy//Paste'

playlists = sp.user_playlists('spotify')
user_playlists = sp.user_playlists(user_id)

def playlister(user, playlists, to_sort):
    pl_uri_list = {}
    while playlists: #gets uri for each playlist 
        for i, playlist in enumerate(playlists['items']):
            # print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))  
            pl_uri_list[playlist['name']] = playlist['uri']
        if playlists['next']:
            playlists = sp.next(playlists)
        else:
            playlists = None

    song_and_art = {} 
    playlist = pl_uri_list[to_sort]
    playlist_items = sp.playlist_items(playlist, market = 'US')

    for song in range(len(playlist_items['items'])):         
        song_uri   = playlist_items['items'][song]['track']['uri']
        song_name = playlist_items['items'][song]['track']['name']
        band_name = playlist_items['items'][song]['track']['album']['name']
        song_art  = playlist_items['items'][song]['track']['album']['images'][0]['url']
        song_and_art[song_uri] = song_art
        
        
    return song_and_art
        

playlister(user = user_id, playlists = user_playlists, to_sort = playlist_to_sort)