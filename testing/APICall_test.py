import unittest
from fn.objectClass import Anime
import fn.APICall as apica
import os, json


class TestStringMethods(unittest.TestCase):
    def test_getDetails(self):
        eplist =  [
    "https://anoboy.online/episode/kuroko-no-basket-s2-episode-001",
    "https://anoboy.online/episode/kuroko-no-basket-s2-episode-002",
    "https://anoboy.online/episode/kuroko-no-basket-s2-episode-003",
    "https://anoboy.online/episode/kuroko-no-basket-s2-episode-004",
    "https://anoboy.online/episode/kuroko-no-basket-s2-episode-005",
    "https://anoboy.online/episode/kuroko-no-basket-s2-episode-006",
    "https://anoboy.online/episode/kuroko-no-basket-s2-episode-007",
    "https://anoboy.online/episode/kuroko-no-basket-s2-episode-008",
    "https://anoboy.online/episode/kuroko-no-basket-s2-episode-009",
    "https://anoboy.online/episode/kuroko-no-basket-s2-episode-010",
    "https://anoboy.online/episode/kuroko-no-basket-s2-episode-011",
    "https://anoboy.online/episode/kuroko-no-basket-s2-episode-012",
    "https://anoboy.online/episode/kuroko-no-basket-s2-episode-013",
    "https://anoboy.online/episode/kuroko-no-basket-s2-episode-014",
    "https://anoboy.online/episode/kuroko-no-basket-s2-episode-015",
    "https://anoboy.online/episode/kuroko-no-basket-s2-episode-016",
    "https://anoboy.online/episode/kuroko-no-basket-s2-episode-017",
    "https://anoboy.online/episode/kuroko-no-basket-s2-episode-018",
    "https://anoboy.online/episode/kuroko-no-basket-s2-episode-019",
    "https://anoboy.online/episode/kuroko-no-basket-s2-episode-020",
    "https://anoboy.online/episode/kuroko-no-basket-s2-episode-021",
    "https://anoboy.online/episode/kuroko-no-basket-s2-episode-022",
    "https://anoboy.online/episode/kuroko-no-basket-s2-episode-023",
    "https://anoboy.online/episode/kuroko-no-basket-s2-episode-024",
    "https://anoboy.online/episode/kuroko-no-basket-s2-episode-025"
  ]
        
        sinopsis = "\n\t\t\tDengan Kejuaraan Interhigh akhirnya berakhir, tim basket Seirin memfokuskan kembali usaha mereka, berlatih lebih keras dari sebelumnya untuk mendapatkan kesempatan untuk berpartisipasi dalam Piala Musim Dingin. Kuroko dan Kagami melihat teman-teman lama berjalan kembali ke kehidupan mereka, memberikan tantangan baik di dalam maupun di luar pengadilan.\r \r Saat keterampilan baru dikembangkan dan aliansi baru diciptakan, musuh dari berbagai tim-raksasa basket sekolah menengah atas seperti Yousen, Shuutoku dan Touou-menghalangi upaya Seirin yang teguh untuk mencapai puncak. Semua sekolah ini terbukti menjadi musuh hebat yang kemampuannya berkembang secara eksponensial, sementara Kuroko berjuang untuk menemukan keseimbangan antara tekadnya untuk bermain sebagai bagian dari sebuah tim dan keinginannya untuk menang.\r \r Dengan luka lama yang membuka kembali, tantangan baru yang harus dihadapi di lapangan, dan serangkaian musuh baru - Raja-Raja yang tidak tenggelam - berusaha mengalahkan para calon baru, apakah Seirin bisa mewujudkan impian mereka untuk mengalahkan Generasi Mujizat?\t\n\t\t"

        anime = Anime("Nonton anime Kuroko No Basket Movie 2: Winter Cup Soushuuhen - Namida No Saki E Sub Indo", "Ended", "Movie","https://anoboy.online/anime/kuroko-no-basket-s2","tmp/s9aqwlyNcBTeVJpCdi5fCLaf6nO.jpg","https://image.tmdb.org/t/p/original/s9aqwlyNcBTeVJpCdi5fCLaf6nO.jpg")
    
        apica.getDetails(anime)
        self.assertEqual(anime.eplist, eplist)

    def test_getDetailss(self):
        eplist =  [
    "https://anoboy.online/episode/kuroko-no-basket-s2-episode-001",
    "https://anoboy.online/episode/kuroko-no-basket-s2-episode-002",
    "https://anoboy.online/episode/kuroko-no-basket-s2-episode-003",
    "https://anoboy.online/episode/kuroko-no-basket-s2-episode-004",
    "https://anoboy.online/episode/kuroko-no-basket-s2-episode-005",
    "https://anoboy.online/episode/kuroko-no-basket-s2-episode-006",
    "https://anoboy.online/episode/kuroko-no-basket-s2-episode-007",
    "https://anoboy.online/episode/kuroko-no-basket-s2-episode-008",
    "https://anoboy.online/episode/kuroko-no-basket-s2-episode-009",
    "https://anoboy.online/episode/kuroko-no-basket-s2-episode-010",
    "https://anoboy.online/episode/kuroko-no-basket-s2-episode-011",
    "https://anoboy.online/episode/kuroko-no-basket-s2-episode-012",
    "https://anoboy.online/episode/kuroko-no-basket-s2-episode-013",
    "https://anoboy.online/episode/kuroko-no-basket-s2-episode-014",
    "https://anoboy.online/episode/kuroko-no-basket-s2-episode-015",
    "https://anoboy.online/episode/kuroko-no-basket-s2-episode-016",
    "https://anoboy.online/episode/kuroko-no-basket-s2-episode-017",
    "https://anoboy.online/episode/kuroko-no-basket-s2-episode-018",
    "https://anoboy.online/episode/kuroko-no-basket-s2-episode-019",
    "https://anoboy.online/episode/kuroko-no-basket-s2-episode-020",
    "https://anoboy.online/episode/kuroko-no-basket-s2-episode-021",
    "https://anoboy.online/episode/kuroko-no-basket-s2-episode-022",
    "https://anoboy.online/episode/kuroko-no-basket-s2-episode-023",
    "https://anoboy.online/episode/kuroko-no-basket-s2-episode-024",
    "https://anoboy.online/episode/kuroko-no-basket-s2-episode-025"
  ]
        
        sinopsis = "\n\t\t\tDengan Kejuaraan Interhigh akhirnya berakhir, tim basket Seirin memfokuskan kembali usaha mereka, berlatih lebih keras dari sebelumnya untuk mendapatkan kesempatan untuk berpartisipasi dalam Piala Musim Dingin. Kuroko dan Kagami melihat teman-teman lama berjalan kembali ke kehidupan mereka, memberikan tantangan baik di dalam maupun di luar pengadilan.\r \r Saat keterampilan baru dikembangkan dan aliansi baru diciptakan, musuh dari berbagai tim-raksasa basket sekolah menengah atas seperti Yousen, Shuutoku dan Touou-menghalangi upaya Seirin yang teguh untuk mencapai puncak. Semua sekolah ini terbukti menjadi musuh hebat yang kemampuannya berkembang secara eksponensial, sementara Kuroko berjuang untuk menemukan keseimbangan antara tekadnya untuk bermain sebagai bagian dari sebuah tim dan keinginannya untuk menang.\r \r Dengan luka lama yang membuka kembali, tantangan baru yang harus dihadapi di lapangan, dan serangkaian musuh baru - Raja-Raja yang tidak tenggelam - berusaha mengalahkan para calon baru, apakah Seirin bisa mewujudkan impian mereka untuk mengalahkan Generasi Mujizat?\t\n\t\t"

        anime = Anime("Nonton anime Kuroko No Basket Movie 2: Winter Cup Soushuuhen - Namida No Saki E Sub Indo", "Ended", "Movie","https://anoboy.online/anime/kuroko-no-basket-s2","tmp/s9aqwlyNcBTeVJpCdi5fCLaf6nO.jpg","https://image.tmdb.org/t/p/original/s9aqwlyNcBTeVJpCdi5fCLaf6nO.jpg")
    
        apica.getDetails(anime)
        self.assertEqual(anime.desc,sinopsis)
             

if __name__ == '__main__':
    unittest.main()

