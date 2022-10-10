import calculator
import unittest


class TestMethods(unittest.TestCase):

    def test_input_validity(self):
        self.assertTrue(calculator.check_validity('3+4-12*197'), 'Valid string')
        self.assertTrue(calculator.check_validity('23 + 13'), 'Valid string with spaces')
        self.assertFalse(calculator.check_validity('text'), 'String with illegal character')
        self.assertFalse(calculator.check_validity('-23-23'), 'String beginning with operator')
        self.assertFalse(calculator.check_validity('43-34-'), 'String ending with operator')
        self.assertFalse(calculator.check_validity('34++34'), 'String with double operators.')

    def test_string_list_conversion(self):

        self.assertEqual(calculator.convert_string_to_list('34+12'), ['34', '+', '12'], 'String no spaces')
        self.assertEqual(calculator.convert_string_to_list('34 + 12'), ['34', '+', '12'], 'String with spaces')
        self.assertEqual(calculator.convert_string_to_list('34+12 - 13'), ['34', '+', '12', '-', '13'],
                         'String with multiple operands and operators')
        self.assertEqual(calculator.convert_string_to_list('34   + 12'), ['34', '+', '12'],
                         'String with different number of spaces before and after the operator')


if __name__ == "__main__":
    unittest.main()
