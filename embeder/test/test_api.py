import unittest
import embed


class TestApi(unittest.TestCase):
    def setUp(self):
        pass

    def test_get_and_default(self):
        doc = embed.get('https://google.com')
        self.assertEqual(doc['default']['title'], u'Google')
        self.assertEqual(doc['default']['desc'], u"Search the world's information, including webpages, images, videos and more. Google has many special features to help you find exactly what you're looking for.")
        self.assertEqual(doc['global']['title'], doc['default']['title'])
        self.assertEqual(doc['global']['desc'], doc['default']['desc'])

    def test_oembed(self):
        doc = embed.get('http://www.youtube.com/watch?v=-r3VuOyr9lk')
        self.assertEqual(doc['oembed']['author_name'], u'ObeyYourSysteM')
        self.assertEqual(doc['oembed']['author_url'],
                         u"http://www.youtube.com/user/ObeyYourSysteM")
        self.assertEqual(doc['oembed']['height'], 344)
        self.assertEqual(doc['oembed']['html'],
                         u'<iframe width="459" height="344" src="http://www.youtube.com/embed/-r3VuOyr9lk?feature=oembed" frameborder="0" allowfullscreen></iframe>')
        self.assertEqual(doc['oembed']['provider_name'], u"YouTube")
        self.assertEqual(doc['oembed']['provider_url'],
                         u"http://www.youtube.com/")
        self.assertEqual(doc['oembed']['thumbnail_height'], 360)
        self.assertEqual(doc['oembed']['thumbnail_url'],
                         u"http://i1.ytimg.com/vi/-r3VuOyr9lk/hqdefault.jpg")
        self.assertEqual(doc['oembed']['thumbnail_width'], 480)
        self.assertEqual(doc['oembed']['title'],
                         u"Serj Tankian - Honking Antelope {Elect The Dead Symphony} (HD/DVD Quality)")
        self.assertEqual(doc['oembed']['type'], u"video")
        self.assertEqual(doc['oembed']['version'], u"1.0")
        self.assertEqual(doc['oembed']['video_url'],
                         u"http://www.youtube.com/embed/-r3VuOyr9lk?feature=oembed")
        self.assertEqual(doc['oembed']['width'], 459)

    def test_opengraph(self):
        doc = embed.get('http://www.youtube.com/watch?v=-r3VuOyr9lk')
        self.assertEqual(doc['opengraph']['desc'],
                         u'SERJ TANKIAN PERFORMING HONKING ANTELOPE Ft APO(AUCKLAND PHILHARMONIA ORCHESTRA) HD QUALITY "ELECT THE DEAD SYMPHONY" DVD RIP{2010}')
        self.assertEqual(doc['opengraph']['picture_url'],
                         u'http://i1.ytimg.com/vi/-r3VuOyr9lk/maxresdefault.jpg')
        self.assertEqual(doc['opengraph']['title'],
                         u'Serj Tankian - Honking Antelope {Elect The Dead Symphony} (HD/DVD Quality)')
        self.assertEqual(doc['opengraph']['video_height'], u'720')
        self.assertTrue(doc['opengraph']['video_url'] in [u'http://www.youtube.com/v/-r3VuOyr9lk?autohide=1&version=3',
                                                          u'http://www.youtube.com/v/-r3VuOyr9lk?version=3&autohide=1'])
        self.assertEqual(doc['opengraph']['video_width'], u'960')

    def test_twitter(self):
        doc = embed.get('http://www.youtube.com/watch?v=-r3VuOyr9lk')
        self.assertEqual(doc['twitter']['desc'], u'SERJ TANKIAN PERFORMING HONKING ANTELOPE Ft APO(AUCKLAND PHILHARMONIA ORCHESTRA) HD QUALITY "ELECT THE DEAD SYMPHONY" DVD RIP{2010}')
        self.assertEqual(doc['twitter']['picture_url'], u"http://i1.ytimg.com/vi/-r3VuOyr9lk/maxresdefault.jpg")
        self.assertEqual(doc['twitter']['title'], u"Serj Tankian - Honking Antelope {Elect The Dead Symphony} (HD/DVD Quality)")
        self.assertEqual(doc['twitter']['video_height'], u"720")
        self.assertEqual(doc['twitter']['video_url'], u"https://www.youtube.com/embed/-r3VuOyr9lk")
        self.assertEqual(doc['twitter']['video_width'], u"960")

    def test_twitter_on_vine(self):
        doc = embed.get('https://vine.co/v/hOjHxFjDznT')
        self.assertEqual(doc['twitter']['desc'], u'Eric and Winston: The Nerd Vandals #prank #nerds #math')
        self.assertEqual(doc['twitter']['picture_url'], u"https://v.cdn.vine.co/r/thumbs/CC17B38DF2981352665344892928_1c699c1c595.3.1.mp4_yIV0ipTC69cV0VOUps_X5I9vltsnSqLHTN7avda3ZyZs7ffQK5nnh8KISf7DPrYj.jpg?versionId=GjdUnkx3BHjGyd_qS1QEOv.AyBFm8MIl")
        self.assertEqual(doc['twitter']['title'], u"Jack and Jack's post on Vine")
        self.assertEqual(doc['twitter']['video_height'], u"435")
        self.assertEqual(doc['twitter']['video_url'], u"https://vine.co/v/hOjHxFjDznT/card")
        self.assertEqual(doc['twitter']['video_width'], u"435")
