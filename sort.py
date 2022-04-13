import io
from urllib.request import urlopen
from sklearn.cluster import KMeans
from collections import Counter
from main import * 
from urllib.request import urlopen
from colorthief import ColorThief

song_and_art = playlister(user_id, user_playlists, playlist_to_sort) 
        
color_dict = {}
        
def sort(saa_dict, palatte = False): 
    for name, url in saa_dict.items(): 
        file_name = name.split(":")[-1]

        art = urlopen(url)
        art_color_prof = io.BytesIO(art.read())
        color_thief = ColorThief(art_color_prof)
        
        art_color = color_thief.get_color(quality=1)
        color_dict[art_color] = file_name 
        
        if palatte: 
            color_thief.get_palatte(quality=1)

    print(color_dict)
    return color_dict

sort(song_and_art)

