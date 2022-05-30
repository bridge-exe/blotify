
import collections
import colorsys
import json
import nntplib
from matplotlib import colors
from dom_color import * 
from scipy.spatial import distance
import numpy as np
import math

# with open('color_dict.txt', 'r') as file:
#     color_dict = json.load(file)
    
colours = []
def inv_lum_colors(color_dict, repetitions = 1):
    print(len(color_dict))
    inv_lum_color_dict = {}
    for key, val in color_dict.items():
        key = eval(key)
        val = val
        r, g, b = key
        
        lum = math.sqrt( .241 * r + .691 * g + .068 * b )
        h, s, v = colorsys.rgb_to_hsv(r,g,b)
        h2 = int(h * repetitions * 100)        
        lum2 = int(lum * repetitions)
        v2 = int(v * repetitions)
        
        if h2 % 2 == 1:
            v2 = repetitions - v2
            lum = repetitions - lum
            
        key = (h2, s, lum, v2, lum2)
        inv_lum_color_dict[key] = val
    # print(inv_lum_color_dict)
    return inv_lum_color_dict

# x = colours.sort(key=lambda r,g,b: inv_lum_colors(r,g,b,8))
# print(x)
  
def sorter(color_dict, inv_lum=True): 
    # print(color_dict)
    tracklist = []
    for key, val in color_dict.items():
        key = eval(key)
        r, g, b = key
        
    if inv_lum: 
        color_dict = inv_lum_colors(color_dict)
    
    # Basic sorter using color tuple in the key of the color dict, with the track listing as the value 
    tupled_sort = {}
    for key, val in color_dict.items():
        # key = eval(key)
        tupled_sort[key] = val
    d = collections.OrderedDict(sorted(tupled_sort.items()))
    for key, v in d.items():
        tracklist.append(v)
        
    # print(tracklist)
    print('Sort done!')
    return tracklist

# sort(color_dict)

