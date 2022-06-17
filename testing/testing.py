import unittest
import function.Scrapper as scrap
from tkinter import Widget
from unittest import IsolatedAsyncioTestCase
from asyncio import events

class TestStringMethods(unittest.TestCase):
    
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
        
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
    
    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        #check that s.split falls when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
    
    def test_decode(self):
        self.assertEqual(scrap.decode_based64("dGVzdGluZw=="), 'testing')
        
    def test_episode(self):
        self.assertEqual(scrap.selectEpisode("https://anoboy.online/episode/heroine-tarumono-kiraware-heroine-to-naisho-no-oshigoto-episode-001#"))
    
    def test_default_widget_size(self):
        widget = Widget('The widget')
        self.assertEqual(widget.size(), (1000, 800))
    
    def setUp(self):
        self.widget = Widget('The widget')

    def test_default_widget_size(self):
        self.assertEqual(self.widget.size(), (50,50),
                         'incorrect default size')

    def test_widget_resize(self):
        self.widget.resize(100,150)
        self.assertEqual(self.widget.size(), (100,150),
                         'wrong size after resize')
        
    async def test_response(self):
        events.append("test_response")
        response = await self._async_connection.get("https://anoboy.online/")
        self.assertEqual(response.status_code, 200)
        self.addAsyncCleanup(self.on_cleanup)
        
    #def test_query(self):
    #    self.assertEqual(scrap.querySearch("1"))
        
if __name__ == '__main__':
    unittest.main()
        