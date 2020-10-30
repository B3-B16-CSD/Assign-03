# pylint: disable=invalid-name
"""
List min replacement
Given a list of integers nums, replace every nums[i]
with the smallest integer left of i. Replace nums[0] with 0.

Example 1
Input
nums = [10, 5, 7, 9]

Output
[0, 10, 5, 5]
"""

import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput


def list_min_replacement(nums):
    


# DO NOT TOUCH THE BELOW CODE
# pylint: disable=unused-variable,line-too-long
class TestListMinReplacement(unittest.TestCase):

    def test_01(self):
        self.assertEqual(list_min_replacement([10, 5, 7, 9]), [0, 10, 5, 5])

    def test_02(self):
        self.assertEqual(list_min_replacement(
            [1, 2, 3, 4, 5, 6]), [0, 1, 1, 1, 1, 1])

    def test_03(self):
        self.assertEqual(list_min_replacement([10]), [0])

    def test_04(self):
        self.assertEqual(list_min_replacement(
            [3, 4, 5, 6, 1, 2]), [0, 3, 3, 3, 3, 1])

    def test_05(self):
        self.assertEqual(list_min_replacement(
            [1, 3, 9, 7, 5, 10, 12]), [0, 1, 1, 1, 1, 1, 1])

    def test_06(self):
        self.assertEqual(list_min_replacement(
            [10, 12, 9, 5, 7, 3, 1]), [0, 10, 10, 9, 5, 5, 3])

    def test_07(self):
        self.assertEqual(list_min_replacement(
            [48, 49, 54, 55, 66, 67, 93, 95, 97, 20, 22, 28, 28, 36, 45]), [0, 48, 48, 48, 48, 48, 48, 48, 48, 48, 20, 20, 20, 20, 20])

    def test_08(self):
        self.assertEqual(list_min_replacement([59, 63, 68, 68, 68, 72, 82, 84, 85, 93, 97, 99, 100,
                                               11, 14, 14, 15, 19, 26, 28, 31, 31, 38, 40, 46, 55, 56, 58, 58, 59]), [0, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11])


if __name__ == '__main__':
    unittest.main(verbosity=2)
