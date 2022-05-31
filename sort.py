
import collections
import colorsys
import json
import nntplib
from matplotlib import colors
from dom_color import * 
from scipy.spatial import distance
import numpy as np
import math
    
colours = []
def inv_lum_colors(color_dict, repetitions=1):
    # color_dict[song_code] = art_color
    inv_lum_color_dict = {}
    for song_code, art_color in color_dict.items():
        art_color = eval(art_color)
        r, g, b = art_color
        lum = math.sqrt( .241 * r + .691 * g + .068 * b )
        h, s, v = colorsys.rgb_to_hsv(r,g,b)
        
        art_color = (h, v, s,lum)
       
        inv_lum_color_dict[song_code] = art_color
   
    return inv_lum_color_dict

def sorter(color_dict): 
    tracklist = []
    # color_dict[song_code] = art_color
    for song_code, art_color in color_dict.items():
        art_color = eval(art_color)
        r, g, b = art_color
        
    color_dict = inv_lum_colors(color_dict)
    
    # Basic sorter using color tuple in the key of the color dict, with the track listing as the value 
    tupled_sort = {}
    for song_code, art_color in color_dict.items():
        tupled_sort[song_code] = art_color
        
    d = {k: v for k, v in sorted(tupled_sort.items(), key=lambda item: item[1])}

    for song_code, v in d.items():
        tracklist.append(song_code)

    print('Sort done!')
    return tracklist

