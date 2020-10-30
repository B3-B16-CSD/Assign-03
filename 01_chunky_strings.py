# pylint: disable=invalid-name
"""
Chunky strings
Given a string s and an integer n, split up s
into n-sized pieces.

For example, given:
s = "abcdefg"
n = 3

Return["abc", "def", "g"].

If there are extra characters left over,
they should be in its own piece.

Example 1
Input
s = "abcdef"
n = 2

Output
["ab", "cd", "ef"]
"""

import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput


def chunky_strings(s, n):
  


# DO NOT TOUCH THE BELOW CODE
# pylint: disable=unused-variable
class TestChunkyStrings(unittest.TestCase):

    def test_01(self):
        self.assertEqual(chunky_strings("abcdef", 2), ["ab", "cd", "ef"])

    def test_02(self):
        self.assertEqual(chunky_strings("abcdefg", 3), ["abc", "def", "g"])

    def test_03(self):
        self.assertEqual(chunky_strings("LHWB", 4), ["LHWB"])

    def test_04(self):
        self.assertEqual(chunky_strings("BwOJu", 3), ["BwO", "Ju"])

    def test_05(self):
        self.assertEqual(chunky_strings("ZelMuuQ", 4), ["ZelM", "uuQ"])

    def test_06(self):
        self.assertEqual(chunky_strings("ucwXwQ", 6), ["ucwXwQ"])

    def test_07(self):
        self.assertEqual(chunky_strings("navzDzYp", 6), ["navzDz", "Yp"])

    def test_08(self):
        self.assertEqual(chunky_strings("EvDjely", 6), ["EvDjel", "y"])


if __name__ == '__main__':
    unittest.main(verbosity=2)
