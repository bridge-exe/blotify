import colorsys
from matplotlib import colors
import matplotlib.colors
from dom_color import * 
from scipy.spatial import distance
import numpy as np
import math
import matplotlib.pyplot as plt

def inv_lum_colors(color_dict):
    inv_lum_color_dict = {}
    for song_code, art_color in color_dict.items():
        rgb_art_color = eval(art_color)
        r, g, b = rgb_art_color
        
        lum = math.sqrt( .241 * r + .691 * g + .068 * b)
        h, s, v = colorsys.rgb_to_hsv(r,g,b)
        
        art_color = (h, s, v, lum)
    
        inv_lum_color_dict[song_code] = art_color
   
    return inv_lum_color_dict

def sorter(color_dict): 
    tracklist = []
    col_palatte = np.empty(shape=(1,3))
    
    tupled_sort_rgb = {}
    for song_code, art_color in color_dict.items():
        art_color = eval(art_color)
        # r, g, b = art_color
        tupled_sort_rgb[song_code] = art_color
        # unsorted_col_palatte = np.vstack((col_palatte, np.array(art_color)))
        
    color_dict_lum = inv_lum_colors(color_dict)
    # Basic sorter using color tuple in the key of the color dict, with the track listing as the value           
    tupled_sort = {}
    for song_code, art_color in color_dict_lum.items():
        tupled_sort[song_code] = art_color
        
    d = {k: v for k, v in sorted(tupled_sort.items(), key=lambda item: item[1])}
  
    for song_code, hsv in d.items():
        tracklist.append(song_code)
        hsv = hsv[0:3]
        rgb = colors.hsv_to_rgb(hsv)
        col_palatte = np.vstack((col_palatte, np.array(rgb)))
    
    # I hate everything below this line # but thank you
    col_palatte = col_palatte[1:]
    col_len = len(col_palatte)
    
    fac_list = []
    for i in range(1, col_len+1):
        if(col_len % i) == 0:
            fac_list.append(i)
    
    if (len(fac_list) % 2 != 0): #if it's odd, it's a square number, so even sides! 
        pal = int(math.sqrt(col_len))
        m,n = pal,pal
        
    elif (len(fac_list) == 2): #if there's only two factors, it's prime, but we need at least two rows still 
        m,n = fac_list[0], fac_list[1]
        
    else: #if it's even, find the middlest two numbers
        i = int(len(fac_list) / 2)
        m,n  = fac_list[i-1], fac_list[i]
    
    indices = np.arange(len(col_palatte) + (m*n - len(col_palatte))).reshape(m,n)
    # print(col_len, ":", fac_list)
    # print(col_palatte)
    # print('\n', indices)
    # print(col_palatte)
    
    for i in range(m*n - len(col_palatte)): 
        # col_palatte = np.vstack((col_palatte, np.array([255,255,255]))
        col_palatte = np.vstack((col_palatte, np.array(col_palatte[0:-1])))
    # print(col_palatte)
    plt.imshow(col_palatte[indices]/255)
    plt.show()
    
    print('Sort done!')
    return tracklist

