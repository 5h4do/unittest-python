import unittest

def add_numbers(x, y):
    return x + y

class TestAddNumbers(unittest.TestCase):

    def test_add_positive_numbers(self):
        result = add_numbers(2, 3)
        self.assertEqual(result, 5)

    def test_add_negative_numbers(self):
        result = add_numbers(-5, -7)
        self.assertEqual(result, -12)

    def test_add_zero(self):
        result = add_numbers(10, 0)
        self.assertEqual(result, 10)

    def test_add_large_numbers(self):
        result = add_numbers(999999999999, 1)
        self.assertEqual(result, 1000000000000)

if __name__ == '__main__':
    runner = unittest.TextTestRunner(resultclass=unittest.TextTestResult)
    result = runner.run(unittest.makeSuite(TestAddNumbers))
    if not result.wasSuccessful():
        print(" ")
