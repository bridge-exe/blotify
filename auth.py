import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd


AUTH_URL = 'https://accounts.spotify.com/api/token'
BASE_URL = 'https://api.spotify.com/v1/'

SPOTIPY_CLIENT_ID= 'ca352b7949dd41018f9fd85dc2aeb024'
SPOTIPY_CLIENT_SECRET= '17314964a6e14136b05c9bdbd9234ae1'
SPOTIPY_REDIRECT_URI= 'http://127.0.0.1:9090'
SCOPE = 'user-top-read'
auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': SPOTIPY_CLIENT_ID,
    'client_secret': SPOTIPY_CLIENT_SECRET,
})
auth_response_data = auth_response.json()

# save the access token
access_token = auth_response_data['access_token']
headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI, scope=SCOPE))

results = sp.user_playlists('spotify')


