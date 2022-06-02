import io
from urllib.request import urlopen
from colorthief import ColorThief
import numpy as np

def dom_col(songs_and_art_url_dict, palatte = True): 
    color_dict = {}
    
    for name in songs_and_art_url_dict: 
        song_code = name.split(":")[-1] #gets the spotify-specific code for the song 

        url = songs_and_art_url_dict[name]
        art = urlopen(url) #opens url for album art 
        art_color_prof = io.BytesIO(art.read()) 
        
        color_thief = ColorThief(art_color_prof)  
        rgb_color = color_thief.get_color(quality=80)
        
        rgb_color_tuple = tuple(rgb_color)
        art_color = str(rgb_color_tuple) #turns object into a tuple, then a str, trust me I had to do this  
        
        color_dict[song_code] = art_color
        print(round(((len(color_dict) / len(songs_and_art_url_dict)*100)),2), '%')
        
    
    print('Colors found!')
    return color_dict


