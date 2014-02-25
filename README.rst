=======
Embeder
=======

Librairy to get the meta informations of a webpage and embed its content.

Typically what happens when you post a video on Facebook or Twitter.


Usage
=====

Command line:

::

    $ python embed.py http://www.youtube.com/watch?v=-r3VuOyr9lk
    {   'default': {   'desc': 'SERJ TANKIAN PERFORMING HONKING ANTELOPE Ft APO(AUCKLAND PHILHARMONIA ORCHESTRA) HD QUALITY "ELECT THE DEAD SYMPHONY" DVD RIP{2010}',
                       'title': u'Serj Tankian - Honking Antelope {Elect The Dead Symphony} (HD/DVD Quality) - YouTube'},
        'global': {   'desc': 'SERJ TANKIAN PERFORMING HONKING ANTELOPE Ft APO(AUCKLAND PHILHARMONIA ORCHESTRA) HD QUALITY "ELECT THE DEAD SYMPHONY" DVD RIP{2010}',
                      'picture_height': 360,
                      'picture_url': 'http://i1.ytimg.com/vi/-r3VuOyr9lk/maxresdefault.jpg',
                      'picture_width': 480,
                      'title': 'Serj Tankian - Honking Antelope {Elect The Dead Symphony} (HD/DVD Quality)',
                      'video_height': '720',
                      'video_url': 'https://www.youtube.com/embed/-r3VuOyr9lk',
                      'video_width': '960'},
        'oembed': {   u'author_name': u'ObeyYourSysteM',
                      u'author_url': u'http://www.youtube.com/user/ObeyYourSysteM',
                      u'height': 344,
                      u'html': u'<iframe width="459" height="344" src="http://www.youtube.com/embed/-r3VuOyr9lk?feature=oembed" frameborder="0" allowfullscreen></iframe>',
                      u'provider_name': u'YouTube',
                      u'provider_url': u'http://www.youtube.com/',
                      u'thumbnail_height': 360,
                      u'thumbnail_url': u'http://i1.ytimg.com/vi/-r3VuOyr9lk/hqdefault.jpg',
                      u'thumbnail_width': 480,
                      u'title': u'Serj Tankian - Honking Antelope {Elect The Dead Symphony} (HD/DVD Quality)',
                      u'type': u'video',
                      u'version': u'1.0',
                      'video_url': 'http://www.youtube.com/embed/-r3VuOyr9lk?feature=oembed',
                      u'width': 459},
        'opengraph': {   'desc': 'SERJ TANKIAN PERFORMING HONKING ANTELOPE Ft APO(AUCKLAND PHILHARMONIA ORCHESTRA) HD QUALITY "ELECT THE DEAD SYMPHONY" DVD RIP{2010}',
                         'picture_url': 'http://i1.ytimg.com/vi/-r3VuOyr9lk/maxresdefault.jpg',
                         'title': 'Serj Tankian - Honking Antelope {Elect The Dead Symphony} (HD/DVD Quality)',
                         'video_height': '720',
                         'video_url': 'http://www.youtube.com/v/-r3VuOyr9lk?version=3&autohide=1',
                         'video_width': '960'},
        'twitter': {   'desc': 'SERJ TANKIAN PERFORMING HONKING ANTELOPE Ft APO(AUCKLAND PHILHARMONIA ORCHESTRA) HD QUALITY "ELECT THE DEAD SYMPHONY" DVD RIP{2010}',
                       'picture_url': 'http://i1.ytimg.com/vi/-r3VuOyr9lk/maxresdefault.jpg',
                       'title': 'Serj Tankian - Honking Antelope {Elect The Dead Symphony} (HD/DVD Quality)',
                       'video_height': '720',
                       'video_url': 'https://www.youtube.com/embed/-r3VuOyr9lk',
                       'video_width': '960'}}

You should use the 'global' values which are a copy of what's available in the different backends unless you want the information provided for a specific format/platform.

To use it in your code, you can do:

::

    import embed
    data = embed.get('http://www.youtube.com/watch?v=-r3VuOyr9lk')


Backends
========

- the default backend retrieves the title and the description metatag of the page
- the oembed backend retrieves some oembed informations: http://oembed.com/
- the opengraph backend retrieves some opengraph metatags: http://ogp.me/
- the twitter backend retrieves some of the twitter metatags: https://dev.twitter.com/docs/cards/markup-reference
