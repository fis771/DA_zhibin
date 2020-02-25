import unittest
import Q6

class TestMyProgram(unittest.TestCase):
    def test_Engine(self):
        vios = Q6.mySpider
        self.assertEqual(vios.parse,'petrol')

if __name__== '__ main __':
     unittest.main()
