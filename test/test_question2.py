import unittest
from src.question2 import Orders
class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.orders_obj = Orders()

    def test_example(self):
        orders = [70, 30, 10]
        n_max = 100
        how_many = self.orders_obj.combine_orders(orders, n_max)
        expected_orders = 2
        self.assertEqual(how_many, expected_orders, 'should be equal')

if __name__ == '__main__':
    unittest.main()