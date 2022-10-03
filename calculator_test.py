import calculator
import unittest


class TestMethods(unittest.TestCase):

    def test_input_validity(self):

        testValue1 = calculator.check_validity('3+4-12*197')
        testValue2 = calculator.check_validity('text')
        testValue3 = calculator.check_validity('-23-23')
        testValue4 = calculator.check_validity('43-34-')
        testValue5 = calculator.check_validity('34++34')

        self.assertTrue(testValue1, 'Valid string')
        self.assertFalse(testValue2, 'String with illegal character')
        self.assertFalse(testValue3, 'String beginning with operator')
        self.assertFalse(testValue4, 'String ending with operator')
        self.assertFalse(testValue5, 'String with double operators.')



