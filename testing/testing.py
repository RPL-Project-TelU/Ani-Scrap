import unittest
import os
import function.Scrapper as scrap
#import urllib.parse, os
#import cloudscraper,re,base64,requests,random
#from bs4 import BeautifulSoup


class TestStringMethods(unittest.TestCase):
    #Testing untuk api_get
    '''def test_api(self)->requests.Response:
        page = scrap.api_get()'''
        
    def Test_downloadFile(self):
        dl = scrap.downloadFile('https://image.tmdb.org/t/p/original/jjS7HGtulytWf4JQD5H53ou3RcM.jpg',"./tmp/")
        self.assertEqual(dl, "jjS7HGtulytWf4JQD5H53ou3RcM.jpg")
    
    
    
    
        
    
    def testing_urlEncode(self)-> str:
        self.assertEqual(scrap.urlEncode('https://anoboy.online/series/healer-girl'))
    
    
    #Testing
    
    # Testing untuk apa