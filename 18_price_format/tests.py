import unittest

from format_price import format_price


class FormatPriceTestCase(unittest.TestCase):
    def test_intstr_to_price(self):
        pretty_price = format_price('123456789')
        self.assertEqual(pretty_price, '123 456 789')

    def test_floatstr_to_price(self):
        pretty_price = format_price('12345.6789')
        self.assertEqual(pretty_price, '12 345.68')

    def test_neg_intstr_to_price(self):
        pretty_price = format_price('-123456789')
        self.assertEqual(pretty_price, '-123 456 789')

    def test_neg_floatstr_to_price_(self):
        pretty_price = format_price('-12345.6789')
        self.assertEqual(pretty_price, '-12 345.68')

    def test_nondigit_to_none(self):
        pretty_price = format_price('1.1a')
        self.assertIsNone(pretty_price)

    def test_none_to_none(self):
        pretty_price = format_price(None)
        self.assertIsNone(pretty_price)

    def test_object_to_none(self):
        pretty_price = format_price([1])
        self.assertIsNone(pretty_price)

    def test_exponential_to_price_(self):
        pretty_price = format_price('123456789e-3')
        self.assertEqual(pretty_price, '123 456.79')

    def test_true_to_price_(self):
        pretty_price = format_price(True)
        self.assertIsNone(pretty_price)

    def test_false_to_price_(self):
        pretty_price = format_price(False)
        self.assertIsNone(pretty_price)


if __name__ == '__main__':
    unittest.main()
