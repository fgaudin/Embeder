import requests
from bs4 import BeautifulSoup


MAPPING = {
   'video_width': 'width',
   'video_height': 'height',
   'picture_url': 'thumbnail_url',
   'picture_width': 'thumbnail_width',
   'picture_height': 'thumbnail_height'
}


def parse(soup, no_request, *args, **kwargs):
    if no_request:
        return {}

    try:
        oembed_link = soup.find('link', {'rel': 'alternate', 'type': 'application/json+oembed'}).attrs['href']
        oembed = requests.get(oembed_link)
        result = oembed.json()
        video_soup = BeautifulSoup(result['html'], 'lxml')
        result['video_url'] = video_soup.find('iframe').attrs['src']
        return result
    except AttributeError:
        pass

    return {}

