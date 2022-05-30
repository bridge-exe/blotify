from matplotlib.colors import rgb_to_hsv

def dom_col(saa_dict, palatte = False): 
    import io
    from urllib.request import urlopen
    from urllib.request import urlopen
    from colorthief import ColorThief
    import json
    color_dict = {}
    for name, url in saa_dict.items(): 
        file_name = name.split(":")[-1]

        art = urlopen(url)
        art_color_prof = io.BytesIO(art.read())
        color_thief = ColorThief(art_color_prof)
        rbg_color = color_thief.get_color(quality=10)
        hsv_color = tuple(rgb_to_hsv(rbg_color))
        
        art_color = str(hsv_color)
        color_dict[art_color] = file_name 
        
        if palatte: 
            color_thief.get_palatte(quality=1)
    
    with open('color_dict.txt', 'w') as convert_file:
        convert_file.write(json.dumps(color_dict))
    print('Colors found!')
    return color_dict


