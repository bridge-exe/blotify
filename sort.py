
import collections
import json
import nntplib
from dom_color import * 
from scipy.spatial import distance
import numpy as np

with open('color_dict.txt', 'r') as file:
    color_dict = json.load(file)
    
def sorter(color_dict): 
    tracklist = []
    
    tupled_sort = {}
    for key, val in color_dict.items():
        key = eval(key)
        tupled_sort[key] = val
        
    d = collections.OrderedDict(sorted(tupled_sort.items()))
    for key, v in d.items():
        tracklist.append(v)
     
    # with open('tracklist.txt', 'w') as output_file:
    #     for track in tracklist:
    #         output_file.write(track + '\n')
    
    
    # print(tracklist)
    print('Sort done!')
    return tracklist

# sort(color_dict)

