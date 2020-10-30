# pylint: disable=invalid-name
"""
Rotate list left by k
Write a function that rotates a list of numbers to the
left by k elements.

For example, [1, 2, 3, 4, 5, 6] rotated by 2
becomes [3, 4, 5, 6, 1, 2]. Numbers should wrap around.

Note: The list is guaranteed to have at least one element,
and k is guaranteed to be less than or equal to the length
of the list.

Example 1
Input
nums = [1, 2, 3, 4, 5, 6]
k = 2

Output
[3, 4, 5, 6, 1, 2]

Example 2
Input
nums = [1, 2, 3, 4, 5, 6]
k = 6

Output
[1, 2, 3, 4, 5, 6]

Example 3
Input
nums = [1]
k = 0

Output
[1]
"""


import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput


def rotate_list(nums, k):
   


# DO NOT TOUCH THE BELOW CODE
# pylint: disable=unused-variable,line-too-long
class TestRotateList(unittest.TestCase):

    def test_01(self):
        self.assertEqual(rotate_list(
            [1, 2, 3, 4, 5, 6], 2), [3, 4, 5, 6, 1, 2])

    def test_02(self):
        self.assertEqual(rotate_list(
            [1, 2, 3, 4, 5, 6], 6), [1, 2, 3, 4, 5, 6])

    def test_03(self):
        self.assertEqual(rotate_list(
            [1], 0), [1])

    def test_04(self):
        self.assertEqual(rotate_list(
            [1, 2, 3, 4, 5, 6], 3), [4, 5, 6, 1, 2, 3])

    def test_05(self):
        self.assertEqual(rotate_list(
            [1, 3, 9, 7, 5, 10, 12], 5), [10, 12, 1, 3, 9, 7, 5])

    def test_06(self):
        self.assertEqual(rotate_list(
            [48, 49, 54, 55, 66, 67, 93, 95, 97, 20, 22, 28, 28, 36, 45], 12), [28, 36, 45, 48, 49, 54, 55, 66, 67, 93, 95, 97, 20, 22, 28])

    def test_07(self):
        self.assertEqual(rotate_list(
            [84, 85, 93, 97, 99, 100, 11, 14, 14, 15, 19, 26, 28, 31, 31, 38, 40, 46, 55, 56, 58, 58, 59, 59, 63, 68, 68, 68, 72, 82], 23), [59, 63, 68, 68, 68, 72, 82, 84, 85, 93, 97, 99, 100, 11, 14, 14, 15, 19, 26, 28, 31, 31, 38, 40, 46, 55, 56, 58, 58, 59])


if __name__ == '__main__':
    unittest.main(verbosity=2)
