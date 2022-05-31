from cv2 import FileNode_NAMED
from matplotlib.colors import rgb_to_hsv
import io
from urllib.request import urlopen
from colorthief import ColorThief

def dom_col(songs_and_art_url_dict, palatte = False): 
    color_dict = {}
        
    for name in songs_and_art_url_dict: 
        song_code = name.split(":")[-1] #gets the spotify-specific code for the song 

        url = songs_and_art_url_dict[name]
        art = urlopen(url) #opens url for album art 
        art_color_prof = io.BytesIO(art.read()) 
        
        color_thief = ColorThief(art_color_prof)  
        rgb_color = color_thief.get_color(quality=23) #given album art, returns (r,g,b) object
        art_color = str(tuple(rgb_color)) #turns object into a tuple, then a str, trust me I had to do this
        
        color_dict[song_code] = art_color
        # if palatte: 
        #     color_thief.get_palatte(quality=1)

    print('Colors found!')
    
    return color_dict


