"""
Created on Wed Sep 18 22:05:55 2019
@author: difusao@gmail.com
"""

import pytube
import os
import sys

video_url=open('links_file.txt','r')
home = os.path.expanduser('~')
download_path = os.path.join(home, 'Downloads/youtube/')
youtube = ""
total = 0
file_size = 0
title = ""
num_lines = sum(1 for line in open('links_file.txt','r'))

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

for url in video_url:
    
    try: 
        youtube = pytube.YouTube(url)
        total += 1
        print
    except: 
        print("Connection Error") #to handle exception 
    
    video = youtube.streams.first()
    file_size = video.filesize            
    vid_title = video.title
    title = '{:03d} Mb - {}'.format((file_size/1024000), vid_title)
    
    youtube.register_on_progress_callback(progress_Check)
    ensure_dir(download_path)
    video.download(download_path)

print
print
print("Task Completed total: %d" %(total))
