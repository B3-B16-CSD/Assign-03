# pylint: disable=invalid-name
"""
Hamming distance
Given two integers x, and y return the number of positions
where their values differ in their binary representations
as a 32-bit integer.

Example 1
Input
x = 9
y = 5

Output
2

Explanation
9 in binary is 1001 and 5 in binary is 0101,
so indices 2 and 3 are different.
"""


import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput


def hamming_distance(x, y):
    b = format(x, '0200b')
    b1 = format(y, '0200b')
    c = 0
    for i in range(0, len(b)):
        if b[i] != b1[i]:
            c += 1
    return c


# DO NOT TOUCH THE BELOW CODE
# pylint: disable=unused-variable
class TestHammingDistance(unittest.TestCase):

    def test_01(self):
        self.assertEqual(hamming_distance(9, 5), 2)

    def test_02(self):
        self.assertEqual(hamming_distance(1, 0), 1)

    def test_03(self):
        self.assertEqual(hamming_distance(0, 0), 0)

    def test_04(self):
        self.assertEqual(hamming_distance(9, 5), 2)

    def test_05(self):
        self.assertEqual(hamming_distance(1506135558, 839263702), 18)

    def test_06(self):
        self.assertEqual(hamming_distance(1347477588, 339414379), 19)

    def test_07(self):
        self.assertEqual(hamming_distance(2112992117, 914837186), 22)

    def test_08(self):
        self.assertEqual(hamming_distance(608826744, 1554748707), 15)


if __name__ == '__main__':
    unittest.main(verbosity=2)
