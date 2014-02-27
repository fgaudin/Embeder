def parse(soup, no_request, *args, **kwargs):
    data = {}

    fields = (
        ('title', 'og:title'),
        ('desc', 'og:description'),
        ('picture_url', 'og:image'),
        ('video_url', 'og:video'),
        ('video_width', 'og:video:width'),
        ('video_height', 'og:video:height'),
    )

    for field in fields:
        try:
            data[field[0]] = soup.find('meta', {'property': field[1]}).attrs['content']
        except:
            pass

    return data
