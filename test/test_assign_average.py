import unittest
from selction_using_dictionary.assign_average import switch_average


class test_swtich_one(unittest.TestCase):
    def test_swtich_average_false(self):
        test_swtich = 'b'
        test_false = switch_average(test_swtich)
        self.assertEqual(test_false, ('The key is not a or b so this is the default value string',False))

class test_swtich_two(unittest.TestCase):
    def test_swtich_average_false(self):
        test_swtich = 'a'
        test_false = switch_average(test_swtich)
        self.assertEqual(test_false, ('The key is not a or b so this is the default value string',False))

class test_swtich_three(unittest.TestCase):
    def test_swtich_average_true(self):
        test_swtich = 'c'
        test_true = switch_average(test_swtich)
        self.assertEqual(test_true, ('The key is not a or b so this is the default value string',True))

class test_swtich_four(unittest.TestCase):
    def test_swtich_average_true(self):
        test_swtich = 'd'
        test_true = switch_average(test_swtich)
        self.assertEqual(test_true, ('The key is not a or b so this is the default value string',True))


if __name__ == '__main__':
    unittest.main()
