from sys import argv
import os

def download_one(link):
    cmd = 'aria2c --max-connection-per-server=16'
    print('$$> Download started:')
    os.system(cmd + " " + link)
    print('$$> Download finished :)')

def download_all(links):
    for link in links:
        download_one(link)
