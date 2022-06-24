import unittest
import function.Scrapper as scrap


class TestStringMethods(unittest.TestCase):

   #Berfungsi untuk mengetes fungsi selectEpisode
   def test_selectEpisode(self):
          self.assertEqual(scrap.selectEpisode,"https://anoboy.online/episode/yuusha-yamemasu-episode-001")
   
   #Berfungsi untuk mengetes fungsi selectMirror
   def test_selectMirror(self):
          self.assertEqual(scrap.selectMirror,"https://core.arc.io/broker.html?94c5673")
   
   
          
          
          
       

if __name__ == '__main__':
    unittest.main()