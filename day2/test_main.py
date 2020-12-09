import unittest

import day2.main as main


class TestPartOne(unittest.TestCase):
    def test_result_correct(self):
        candidates = main.read_file(unc_path='./test_input_part1.txt')
        self.assertEqual(2, main.num_of_valid_pw(candidates=candidates,
                                                 criteria='part1'))


class TestPartTwo(unittest.TestCase):
    def test_result_correct(self):
        candidates = main.read_file(unc_path='./test_input_part2.txt')
        self.assertEqual(2, main.num_of_valid_pw(candidates=candidates,
                                                 criteria='part2'))


if __name__ == '__main__':
    unittest.main()
