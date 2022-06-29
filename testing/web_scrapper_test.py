import unittest
from function import webScrapper as webscrap

class TestStringMethods(unittest.TestCase):
#Berfungsi untuk mengetes anime yang baru diupload 
    def test_recent(self):
        page = webscrap.recent("https://anoboy.online/")
        Anime = ["Ao Ashi","Ashito Aoi adalah pesepakbola muda yang bercita-cita tinggi dari kota terpencil di Jepang. Harapannya untuk masuk ke SMA dengan klub sepak bola yang bagus pupus ketika dia menyebabkan insiden dalam pertandingan penting timnya, yang mengakibatkan kekalahan dan tim mereka gugur dari turnamen. Namun ternyata dia menarik perhatian Tatsuya Fukuda, pelatih tim SMA dari tim muda J-League terkemuka, Tokyo City Esperion FC. Setelah itu Tatsuya menjelaskan ambisinya pada Aoi kalau dia ingin membangun tim yang dapat menguasai dunia.","https://anoboy.online/series/ao-ashi"]
        self.assertEqual(page,Anime)

    #Berfungsi untuk mengetes  penambahan episode list
    #dan sinopsis ke objek anime
    def test_getDetails(self):
        page = webscrap.getDetails("https://anoboy.online/")
        self.assertEqual(page)
    
    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())

    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

if __name__ == '__main__':
    unittest.main()