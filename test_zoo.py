import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_error(self):
        self.assertEqual(self.zoo.get_ticket_price(-1), "Error")

    def test_0_12(self):
        self.assertEqual(self.zoo.get_ticket_price(0), 50) 
        self.assertEqual(self.zoo.get_ticket_price(10), 50) 
    
    def test_13_20(self):
        self.assertEqual(self.zoo.get_ticket_price(13), 100)
        self.assertEqual(self.zoo.get_ticket_price(20), 100) 
    
    def test_21_60(self):
        self.assertEqual(self.zoo.get_ticket_price(21), 150)  
    
    def test_60plus(self):
        self.assertEqual(self.zoo.get_ticket_price(61), 100)  

if __name__ == '__main__':
    unittest.main()