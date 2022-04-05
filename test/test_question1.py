import unittest
from src.question1 import Contract, Contracts

class TestContracts(unittest.TestCase):

    def setUp(self):
       self.contracts_obj = Contracts()
       self.contracts = [
            Contract(1, 3),
            Contract(2, 5),
            Contract(3, 66),
            Contract(6, 7),
            Contract(5, 15),
            Contract(4, 10)
        ]

    def test_example(self):
        renegotiated = [3]
        top_n = 3
        actual_open_contracts = self.contracts_obj.get_top_N_open_contracts(
            self.contracts, renegotiated, top_n
        )
        expected_open_contracts = [5, 4, 6]
        self.assertEqual(actual_open_contracts, expected_open_contracts, 'should be equal')
    
    def test_without_renegotiated(self):
        renegotiated = []
        top_n = 3
        actual_open_contracts = self.contracts_obj.get_top_N_open_contracts(
            self.contracts, renegotiated, top_n
        )
        expected_open_contracts = [3, 5, 4]
        self.assertEqual(actual_open_contracts, expected_open_contracts, 'should be equal')

    def test_with_all_renegotiated(self):
        renegotiated = [1, 2, 3, 4, 5, 6]
        top_n = 3
        actual_open_contracts = self.contracts_obj.get_top_N_open_contracts(
            self.contracts, renegotiated, top_n
        )
        expected_open_contracts = []
        self.assertEqual(actual_open_contracts, expected_open_contracts, 'should be equal')

    def test_top_n_bigger_than_list_size(self):
        renegotiated = [4, 5, 1]
        top_n = 10000
        actual_open_contracts = self.contracts_obj.get_top_N_open_contracts(
            self.contracts, renegotiated, top_n
        )
        expected_open_contracts = [3, 6, 2]
        self.assertEqual(actual_open_contracts, expected_open_contracts, 'should be equal')


if __name__ == '__main__':
    unittest.main()