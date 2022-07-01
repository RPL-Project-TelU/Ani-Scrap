import unittest
import api.APIController as apic
import os, json

class TestStringMethods(unittest.TestCase):    
    
    def testQuerySearch(self):
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
        self.assertEqual(apic.querySearch("spy"), json.loads(expected))
    
if __name__ == '__main__':
    unittest.main()