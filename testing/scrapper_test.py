import unittest
import function.Scrapper as scrap

class TestStringMethods(unittest.TestCase):

    def test_decode(self):
        self.assertEqual(scrap.decode_base64("dGVzdGluZw=="), 'testing')

    def test_parse(self):
        page = scrap.parse_web("https://example.com/")
        self.assertEqual(page.find('h1').text, "Example Domain")
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