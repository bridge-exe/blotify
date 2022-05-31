import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
from auth import *
from dom_color import *
from sort import sorter

#Please input your client_id, secret, and your personal user_id. 
# print('Please input your client_id, secret, and your personal user_id. ')
# client_id = str(input("Your client ID: "))
# secret = str(input("Your client secret: "))
# user_id = str(input("Your user ID: "))

auth = SpotifyClientCredentials(client_id, secret)
sp = spotipy.Spotify(auth_manager=auth)

# playlist_to_sort = str(input("Exact name of PUBLIC playlist to sort: "))

playlists = sp.user_playlists('spotify', limit = 50)
user_playlists = sp.user_playlists(user_id) 

def get_playlist_tracks(u, playlist_id):
    results = sp.playlist_items(playlist_id=playlist_id, market = 'us')
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])    
    return tracks

def playlister(user, playlists, playlist_to_sort):
    pl_uri_list = {}
    while playlists: #gets uri for each playlist 
        for i, playlist in enumerate(playlists['items']):
            pl_uri_list[playlist['name']] = playlist['uri']
        if playlists['next']:
            playlists = sp.next(playlists)
        else:
            playlists = None            
   
    song_and_art = {} 
    playlist = pl_uri_list[playlist_to_sort]
    playlist_items = get_playlist_tracks(user_id, playlist_id = playlist)

    for song in range(len(playlist_items)):       
        song_uri   = playlist_items[song]['track']['uri']
        # # song_name = playlist_items[song]['track']['name']
        # # band_name = playlist_items[song]['track']['album']['name']
        song_art  = playlist_items[song]['track']['album']['images'][0]['url']
        song_and_art[song_uri] = song_art
        
    print('Playlister done!')
    return song_and_art

p = playlister(user_id, user_playlists, playlist_to_sort)
d = dom_col(p)
tracklist = sorter(d)

if len(tracklist) > 2: 
    sorted_playlist = playlist_to_sort + '-Sorted ILum'
    new_list = sp.user_playlist_create(user_id, sorted_playlist)

    playlist_id = new_list["id"]
    
    if len(tracklist) < 50:
        sp.playlist_add_items(playlist_id, tracklist)
    
    else: 
        lower = 0
        upper = 10 
        bound = range(round(int(len(tracklist))/10) + 1)
        for i in bound:
            tracks_100 = tracklist[lower:upper]
            # print(tracks_100)
            if (tracks_100 != []): 
                sp.playlist_add_items(playlist_id, tracks_100)
            lower+=10
            upper+=10
    
    print('Playlist done! Check your Spotify!')
