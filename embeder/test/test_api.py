import unittest
import embeder


class TestApi(unittest.TestCase):
    def setUp(self):
        pass

    def test_get(self):
        doc = embeder.get('https://pypi.python.org/pypi')
        self.assertTrue(True)
