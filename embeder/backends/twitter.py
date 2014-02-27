def parse(soup, no_request, *args, **kwargs):
    data = {}

    fields = (
        ('title', 'twitter:title'),
        ('desc', 'twitter:description'),
        ('picture_url', 'twitter:image'),
        ('video_url', 'twitter:player'),
        ('video_width', 'twitter:player:width'),
        ('video_height', 'twitter:player:height'),
    )

    for field in fields:
        try:
            data[field[0]] = soup.find('meta', {'name': field[1]}).attrs['content']
        except:
            try:
                data[field[0]] = soup.find('meta', {'property': field[1]}).attrs['content']
            except:
                pass

    return data
