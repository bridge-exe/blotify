import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
from auth import *
from dom_color import *
from sort import sorter
import os

#
print('Please input your client_id, secret, and your personal user_id.\n') 
client_id = str(input("Your client ID: "))
secret = str(input("Your client secret: "))
user_is = str(input("Your user ID"))
playlist_to_sort = str(input("Exact name of playlist to sort:"))
# playlist_to_sort = ''


auth = SpotifyClientCredentials(client_id, secret)
sp = spotipy.Spotify(auth_manager=auth)



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
        
    print('playlister done')
    return song_and_art
    
# spotify_client = SpotifyClient(os.getenv("SPOTIFY_AUTHORIZATION_TOKEN"),
#                                    os.getenv("SPOTIFY_USER_ID"))
p = playlister(user_id, user_playlists, playlist_to_sort)
d = dom_col(p)
tracklist = sorter(d)

if len(tracklist) > 0: 
    sorted_playlist = playlist_to_sort + ' Sorted HSV'
    new_list = sp.user_playlist_create(user_id, sorted_playlist)

    playlist_id = new_list["id"]
    sp.playlist_add_items(playlist_id, tracklist)
