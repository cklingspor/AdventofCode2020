import unittest
import utils


class MyTestCase(unittest.TestCase):
    def test_something(self):
        input = utils.read_file(unc_path='./test_input.txt')
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
