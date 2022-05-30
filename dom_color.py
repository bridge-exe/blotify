from matplotlib.colors import rgb_to_hsv
def dom_col(saa_dict, palatte = False): 
    import io
    from urllib.request import urlopen
    from urllib.request import urlopen
    from colorthief import ColorThief
    print('b4 dom col', len(saa_dict))
    color_dict = {}
    for name, url in saa_dict.items(): 
        file_name = name.split(":")[-1]

        art = urlopen(url)
        art_color_prof = io.BytesIO(art.read())
        color_thief = ColorThief(art_color_prof)
        rgb_color = color_thief.get_color(quality=5)
        
        art_color = str(tuple(rgb_color))
        # hsv_color = tuple(rgb_to_hsv(rgb_color))
        # art_color = str(hsv_color)
        
        color_dict[art_color] = file_name 
        
        if palatte: 
            color_thief.get_palatte(quality=1)
    
    print('after dom col', len(color_dict))
    print('Colors found!')
    
    return color_dict


