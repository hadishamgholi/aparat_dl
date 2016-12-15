#!/usr/bin/env python3
import scraper
import downloader
import sys


if __name__ == "__main__":
    argv = sys.argv
    print(argv[1])
    links = scraper.get_links(argv[1])
    print(links)
