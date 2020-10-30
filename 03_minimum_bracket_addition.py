# pylint: disable=invalid-name
"""
Minimum Bracket Addition
Given a string s containing brackets ( and ),
return the minimum number of brackets that
can be inserted so that the brackets are balanced.


Example 1
Input
s = ")))(("

Output
5

Explanation
We can insert ((( to the front and )) to the end
"""


import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput


def minimum_bracket_addition(s):



# DO NOT TOUCH THE BELOW CODE
# pylint: disable=unused-variable,line-too-long
class TestMinimumBracketAddition(unittest.TestCase):

    def test_01(self):
        self.assertEqual(minimum_bracket_addition(")))(("), 5)

    def test_02(self):
        self.assertEqual(minimum_bracket_addition(""), 0)

    def test_03(self):
        self.assertEqual(minimum_bracket_addition("())(((((((("), 9)

    def test_04(self):
        self.assertEqual(minimum_bracket_addition(
            "))()))(()((((()())()))()()))))()))(("), 10)

    def test_05(self):
        self.assertEqual(minimum_bracket_addition(
            ")))())(()))))()))((((((((()))(())(()))))()((((("), 17)

    def test_06(self):
        self.assertEqual(minimum_bracket_addition(
            "()))(((()))((()())(()((()()(()(()))))((((())((((()(()(((())(()("), 17)

    def test_07(self):
        self.assertEqual(minimum_bracket_addition(
            "()))())))))))((())((()))()((((((((((()((((())((((()((((()(())()("), 32)

    def test_08(self):
        self.assertEqual(minimum_bracket_addition(
            "()))()))(()(()(())())(()(())()(((()()()((()((()(()())((()((()(())(()))())))((((()))(())()"), 15)


if __name__ == '__main__':
    unittest.main(verbosity=2)
