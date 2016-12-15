from sys import argv
import os

def download_one(link):
    cmd = 'youtube-dl --external-downloader aria2c \
            --external-downloader-args \
            --max-connection-per-server=16'
    os.system(cmd + " " + link)

def download_all(links):
    for link in links:
        download_one(link)
