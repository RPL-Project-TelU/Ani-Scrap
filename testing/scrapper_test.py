import unittest
import fn.Scrapper as scrap
import os, json

class TestStringMethods(unittest.TestCase):

    def test_decode(self):
        self.assertEqual(scrap.decode_base64("dGVzdGluZw=="), 'testing')

    def test_encode(self):
        self.assertEqual(scrap.encode_base64('testing'), 'dGVzdGluZw')

    def test_apiGet(self):
        expected = """
        {
            "Nonton anime Release the Spyce Sub Indo": {
            "episode": "Anime",
            "link": "https://anoboy.online/anime/release-the-spyce",
            "status": "Ended",
            "thumb": "tmp/iF9BWH60Mxsl831GeSiitkVKYP3.jpg",
            "thumb_link": "https://image.tmdb.org/t/p/original/iF9BWH60Mxsl831GeSiitkVKYP3.jpg"
            },
            "Nonton anime Spy no Tsuma Sub Indo": {
            "episode": "Movie",
            "link": "https://anoboy.online/movie/spy-no-tsuma",
            "status": "Ended",
            "thumb": "tmp/lnK7Q030BIOmAqZvaNfK4aNv8f9.jpg",
            "thumb_link": "https://image.tmdb.org/t/p/original/lnK7Q030BIOmAqZvaNfK4aNv8f9.jpg"
            },
            "Nonton anime Spy x Family Sub Indo": {
            "episode": "12",
            "link": "https://anoboy.online/anime/spy-x-family",
            "status": "Ended",
            "thumb": "tmp/121382.th.jpg",
            "thumb_link": "https://img.topddl.net/images/2022/04/09/121382.th.jpg"
            }
        }
        """
        self.assertEqual(scrap.api_get("http://127.0.0.1:5000/search-anime/spy").json(), json.loads(expected))

    def test_parse(self):
        page = scrap.parse_web("https://example.com/")
        self.assertEqual(page.find('h1').text, "Example Domain")

    def test_downloadFilePictureExist(self):
        dl = scrap.downloadFile("https://image.tmdb.org/t/p/original/oz5upj4Be6u0WVKFUOObEggNcJ5.jpg", './tmp/')
        self.assert_(os.path.isfile("./tmp/oz5upj4Be6u0WVKFUOObEggNcJ5.jpg"))
    
    def test_downloadFilePictureNotExist(self):
        os.remove("./tmp/oz5upj4Be6u0WVKFUOObEggNcJ5.jpg")
        dl = scrap.downloadFile("https://image.tmdb.org/t/p/original/oz5upj4Be6u0WVKFUOObEggNcJ5.jpg", './tmp/')
        self.assert_(os.path.isfile("./tmp/oz5upj4Be6u0WVKFUOObEggNcJ5.jpg"))
    
    def test_downloadFileNotPicture(self):
        dl = scrap.downloadFile("https://github.com/RPL-Project-TelU/Ani-Scrap", "./tmp/")
        self.assertEqual(dl, '')

if __name__ == '__main__':
    unittest.main()