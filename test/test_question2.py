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

    def test_example_2(self):
        orders = [30, 80, 15, 1, 100, 70, 50, 50]
        n_max = 100
        how_many = self.orders_obj.combine_orders(orders, n_max)
        expected_orders = 6
        self.assertEqual(how_many, expected_orders, 'should be equal')

    def test_example_3(self):
        orders = [30, 80, 15, 1, 100, 70, 50, 50]
        n_max = 200
        how_many = self.orders_obj.combine_orders(orders, n_max)
        expected_orders = 4
        self.assertEqual(how_many, expected_orders, 'should be equal')

    def test_example_4(self):
        orders = [30, 80, 15, 80, 70, 70, 50, 50]
        n_max = 80
        how_many = self.orders_obj.combine_orders(orders, n_max)
        expected_orders = 8
        self.assertEqual(how_many, expected_orders, 'should be equal')


if __name__ == '__main__':
    unittest.main()