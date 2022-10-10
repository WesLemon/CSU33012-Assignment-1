import calculator
import unittest


class TestMethods(unittest.TestCase):

    def test_list_validity(self):
        self.assertTrue(calculator.check_validity(['3', '+', '4', '-', '12', '*', '197']), 'Valid list')
        self.assertTrue(calculator.check_validity(['23', '+', '13']), 'Valid list with spaces')
        self.assertTrue(calculator.check_validity(['-23', '*', '5']), 'Valid list with negative number')
        self.assertTrue(calculator.check_validity(['-29', '*', '-29']), 'Valid list with only negative numbers')
        self.assertFalse(calculator.check_validity(['t', 'e', 'x', 't']), 'List with illegal characters')
        self.assertFalse(calculator.check_validity(['+', '23', '-', '23']), 'List beginning with operator')
        self.assertFalse(calculator.check_validity(['43', '-', '34', '-']), 'List ending with operator')
        self.assertFalse(calculator.check_validity(['34', '+', '+', '34']), 'List with double operators.')

    def test_string_list_conversion(self):
        self.assertEqual(calculator.convert_string_to_list('34+12'), ['34', '+', '12'], 'String no spaces')
        self.assertEqual(calculator.convert_string_to_list('34 + 12'), ['34', '+', '12'], 'String with spaces')
        self.assertEqual(calculator.convert_string_to_list('34+12 - 13'), ['34', '+', '12', '-', '13'],
                         'String with multiple operands and operators')
        self.assertEqual(calculator.convert_string_to_list('34   + 12'), ['34', '+', '12'],
                         'String with different number of spaces before and after the operator')
        self.assertIsNone(calculator.convert_string_to_list('32 32'), 'String with double operands')
        self.assertEqual(calculator.convert_string_to_list('-32 * 5'), ['-32', '*', '5'],
                         'String with a negative number'),
        self.assertIsNone(calculator.convert_string_to_list('23 + - * 34'),
                          'String with operator minus sign between two operators')
        self.assertIsNone(calculator.convert_string_to_list('text'), 'String with invalid characters')


if __name__ == "__main__":
    unittest.main()
