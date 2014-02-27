def parse(soup, no_request, *args, **kwargs):
    data = {}

    try:
        data['title'] = soup.find('title').text
    except:
        pass

    try:
        data['desc'] = soup.find('meta', {'name': 'description'}).attrs['content']
    except:
        data['desc'] = ''

    return data
