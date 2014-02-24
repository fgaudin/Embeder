def parser(soup):
    data = {}

    try:
        data['title'] = soup.title.text,
    except:
        pass

    try:
        data['desc'] = soup.find('meta', {'name': 'description'}).attrs['content']
    except:
        pass

    return data
