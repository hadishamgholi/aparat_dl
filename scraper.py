import requests
from bs4 import BeautifulSoup


def get_links(url):
    html = requests.get(url).content
    soup = BeautifulSoup(html, "html.parser")
    a_tags = soup.select('li.download-link > a')

    links = []
    for a_tag in a_tags:
        quality = a_tag.text.strip()
        link = a_tag['href'].strip()
        links = links + [(quality, link)]

    return links
