import unittest
import pandas as pd
from main import phone_prefix_match as ppm
from main import min_price_operator_checker as mpoc


class MyTestCase(unittest.TestCase):
    def test_something(self):
        operator1 = {0: ['1', '43', '432', '4256'],
                     1: ['0.1', '1.0', '1.3', '0.6']}
        operator2 = {0: ['1', '42', '432', '4256'],
                     1: ['0.9', '1.1', '1.2', '0.5']}
        pd_op1 = pd.DataFrame.from_dict(operator1)
        pd_op2 = pd.DataFrame.from_dict(operator2)
        data_dict = {'operator1': pd_op1, 'operator2': pd_op2}
        phone_no = '432678943'
        expected_res = {'operator1': '1.3', 'operator2': '1.2'}
        obtained_res = ppm(data_dict, phone_no)
        self.assertDictEqual(expected_res, obtained_res)
        expected_min_operator = 'operator2'
        expected_min_price = '1.2'
        obtained_min_operator, obtained_min_price = mpoc(expected_res)
        self.assertEqual(expected_min_operator, obtained_min_operator)
        self.assertEqual(expected_min_price, obtained_min_price)


if __name__ == '__main__':
    unittest.main()
