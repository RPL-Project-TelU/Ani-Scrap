import unittest
import function.Scrapper as scrap
import os

class TestStringMethods(unittest.TestCase):

    def test_decode(self):
        self.assertEqual(scrap.decode_base64("dGVzdGluZw=="), 'testing')

    def test_parse(self):
        page = scrap.parse_web("https://example.com/")
        self.assertEqual(page.find('h1').text, "Example Domain")

    def test_downloadFile(self):
        dl = scrap.downloadFile("https://image.tmdb.org/t/p/original/oz5upj4Be6u0WVKFUOObEggNcJ5.jpg", './tmp/')
        self.assert_(os.path.isfile("./tmp/oz5upj4Be6u0WVKFUOObEggNcJ5.jpg"))

if __name__ == '__main__':
    unittest.main()