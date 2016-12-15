#!/usr/bin/env python3
import scraper
import downloader
from sys import argv, exit


if __name__ == "__main__":
    links = scraper.get_links(argv[1])
    i = 1
    for link in links:
        print(i, link[0])
        print(link[1])
        i = i + 1
    inp = int(input("Select Quality: "))
    if inp < 1 or inp > len(links):
        print("Invalid selection!")
        sys.exit(1)
    link = links[inp-1][1]
    downloader.download_one(link)
