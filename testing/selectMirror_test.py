import unittest
import fn.webScrapper as scrap
import re

class TestStringMethods(unittest.TestCase):    
    def testselectMirror(self):
        self.assert_(re.search("http.*",scrap.selectMirror("https://anoboy.online/episode/kumichou-musume-to-sewagakari-episode-001#")))
    
if __name__ == '__main__':
    unittest.main()
    

