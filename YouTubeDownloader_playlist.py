"""
Created on Fri Sep 20 22:19:19 2019
@author: difusao@gmail.com
SO: Linux
"""

import pytube
import os
import sys

video_url = open('links_file_playlist.txt','r')
total = 0
items = 0
youtube = ""
home = os.path.expanduser('~')
download_path = os.path.join(home, 'Downloads/youtube/')
file_size = 0
title = ""
urls = ""

def progress_Check(stream = None, chunk = None, file_handle = None, remaining = None):	
    percent = (100*(file_size-remaining))/file_size
    print("    {:03d}% - {}".format(percent, title))
    sys.stdout.write("\033[F")
    
def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

# make dir default
ensure_dir(download_path)

for i in video_url:
    try:        
        pl = pytube.Playlist(i)
        
        titlePlaylist = pl.title()        
        pl.populate_video_urls()
        urls = pl.video_urls        
        print
        print("[%03d] Title playlist: %s" %(len(pl.video_urls), titlePlaylist))
        
        total += 1
    except: 
        print("Connection Error")
    
    try:
        for url in urls:
            youtube = pytube.YouTube(url)
            video = youtube.streams.first()
            
            file_size = video.filesize
            
            vid_title = video.title            
            title = '{:03d} Mb - {}'.format((file_size/1024000), vid_title)
            
            youtube.register_on_progress_callback(progress_Check)
            ensure_dir(download_path + titlePlaylist + '/')
            video.download(download_path + titlePlaylist + '/')
            
            items += 1
            print
    except: 
        print("Some Error!\n") 
#print
print("Task Completed! \nPlaylists:%2d \nVideos:%2d" %(total, items))
print