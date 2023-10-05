import unittest
import sys
import random as rnd
sys.path.insert(0, '../../src')  # noqa
import my_utils


class TestMyUtils(unittest.TestCase):
    def test_mean(self):
        # Generate large list of random integers
        rnums = [rnd.randint(0, 100) for i in range(10000)]
        dir_mean = sum(rnums) / len(rnums)
        func_mean = my_utils.mean(rnums)
        self.assertEqual(dir_mean, func_mean)

    def test_mean_emptyinput(self):
        self.assertIsNone(my_utils.mean([]))

    def test_mean_incorrectinput(self):
        str_list = ['only', 'strings', 'here']
        self.assertIsNone(my_utils.mean(str_list))

    def test_mean_mixedinput(self):
        inp_list = [1, 5.2, '9.3', 'string', 4]
        dir_mean = (1 + 5.2 + 9.3 + 4) / 4
        self.assertEqual(my_utils.mean(inp_list), dir_mean)

    def test_mean_neginput(self):
        # Generate large list of random integers
        rnums = [rnd.randint(-100, 100) for i in range(100000)]
        func_mean = my_utils.mean(rnums)
        equal = False
        if func_mean >= -0.5 and func_mean <= 0.5:
            equal = True
        self.assertTrue(func_mean, 0)

    def test_median(self):
        # Generate large list of random integers
        rnums = [rnd.randint(-100, 100) for i in range(100000)]
        # Median of random list of integers from -100 to 100 should be ~0
        equal = False
        med = my_utils.median(rnums)
        if med >= -1 and med <= 1:
            equal = True
        self.assertTrue(equal)

    def test_median_emptyinput(self):
        self.assertIsNone(my_utils.median([]))

    def test_median_incorrectinput(self):
        str_list = ['no', 'numbers', 'here']
        self.assertIsNone(my_utils.median(str_list))

    def test_median_mixedinput(self):
        inp_list = ['a.de', '3.2', 6, 3, '4']
        self.assertEqual(my_utils.median(inp_list), 3.6)

    def test_stdeviation(self):
        rnums = [rnd.randint(-100, 100) for i in range(10000)]
        # Stdev approaches sqrt((b-a)^2/12) for uniform distribution
        theory_stdev = pow(pow(100 + 100, 2) / 12, 0.5)
        func_stdev = my_utils.stdeviation(rnums)
        equal = False
        if func_stdev >= theory_stdev - 0.5 \
                and func_stdev <= theory_stdev + 0.5:
            equal = True
        self.assertTrue(func_stdev, theory_stdev)

    def test_stdeviation_emptyinput(self):
        self.assertIsNone(my_utils.stdeviation([]))

    def test_stdeviation_incorrectinput(self):
        str_list = ['just', 'words', 'this', 'time']
        self.assertIsNone(my_utils.stdeviation(str_list))


if __name__ == '__main__':
    unittest.main()
