from main import * 
import requests # to get image from the web
import shutil # to save it locally
import os

song_and_art = playlister(user_id, user_playlists, playlist_to_sort) 
images = 'playlist-images'
os.makedirs(images, exist_ok = True)

def snapper(file_path = images):
    for f in os.listdir(file_path):
        os.remove(os.path.join(file_path, f))
        
def downloader(saa_dict): 
    snapper()
    for name, url in saa_dict.items(): 
        file_name = images + '/' + name.split(":")[-1] + '.jpg'
        res = requests.get(url, stream = True)

        if res.status_code == 200:
            with open(file_name,'ab') as f:
                shutil.copyfileobj(res.raw, f)
            print('Image sucessfully Downloaded: ',file_name)
        else:
            print('Image Couldn\'t be retrieved')
    return 
     
# downloader(song_and_art)