import unittest
import function.Scrapper as scrap
import function.Scrapper as Scrapper
import os

class TestStringMethods(unittest.TestCase):
    
    #Berfungsi untuk mengetes fungsi decode_base64
    def test_decode(self):
        self.assertEqual(scrap.decode_base64("dGVzdGluZw=="), 'testing')
        
    #Berfungsi untuk mengetes fungsi parse_web
    def test_parse(self):
        page = scrap.parse_web("https://example.com/")
        self.assertEqual(page.find('h1').text, "Example Domain")
    
    #Berfungsi untuk mengetes apakah bisa mendownload file
    #apabila gambarnya tersedia
    def test_downloadFilePictureExist(self):
        dl = scrap.downloadFile("https://image.tmdb.org/t/p/original/oz5upj4Be6u0WVKFUOObEggNcJ5.jpg", './tmp/')
        self.assert_(os.path.isfile("./tmp/oz5upj4Be6u0WVKFUOObEggNcJ5.jpg"))
    
    #Berfungsi untuk mengetes apakah bisa mendownload file
    #apabila gambarnya tidak tersedia
    def test_downloadFilePictureNotExist(self):
        os.remove("./tmp/oz5upj4Be6u0WVKFUOObEggNcJ5.jpg")
        dl = scrap.downloadFile("https://image.tmdb.org/t/p/original/oz5upj4Be6u0WVKFUOObEggNcJ5.jpg", './tmp/')
        self.assert_(os.path.isfile("./tmp/oz5upj4Be6u0WVKFUOObEggNcJ5.jpg"))
    
    #Berfungsi untuk mengetes apakah bisa mendownload file
    #apabila tidak ada gambarnya
    def test_downloadFileNotPicture(self):
        dl = scrap.downloadFile("https://github.com/RPL-Project-TelU/Ani-Scrap", "./tmp/")
        self.assertEqual(dl, '')
    
    
    '''data = {
        "page" : 0,
        "limit" : 21,
        "action" : "load_search_movie",
        "keyword" : "testing",
    }
    
    page = Scrapper.urlEncode("https://anoboy.online/",data)
    print(page)'''
 

if __name__ == '__main__':
    unittest.main()