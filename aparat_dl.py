#!/usr/bin/env python3
import scraper
import downloader
from sys import argv


if __name__ == "__main__":
    links = scraper.get_links(argv[1])
    print(links)
