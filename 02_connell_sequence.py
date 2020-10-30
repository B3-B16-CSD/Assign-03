"""
The Connell sequence is a sequence made by:

Taking the first odd integer: 1
Taking the next two even integers 2, 4
Taking the next three odd integers 5, 7, 9
Taking the next four even integers 10, 12, 14, 16
And so on.
Given an integer n, return the nth (0-indexed) term of this sequence.

Example 1
Input
n = 2

Output
4

Explanation
The sequence starts with [1, 2, 4]
"""
import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput


def connell_sequence(n):
   


# DO NOT TOUCH THE BELOW CODE
class TestConnellSequence(unittest.TestCase):

    def test_01(self):
        self.assertEqual(connell_sequence(2), 4)

    def test_02(self):
        self.assertEqual(connell_sequence(0), 1)

    def test_03(self):
        self.assertEqual(connell_sequence(10), 17)

    def test_04(self):
        self.assertEqual(connell_sequence(37), 67)

    def test_05(self):
        self.assertEqual(connell_sequence(159), 302)

    def test_06(self):
        self.assertEqual(connell_sequence(834), 1629)

    def test_07(self):
        self.assertEqual(connell_sequence(3863), 7640)

    def test_08(self):
        self.assertEqual(connell_sequence(9997), 19855)

    def test_09(self):
        self.assertEqual(connell_sequence(1489), 2925)


if __name__ == '__main__':
    unittest.main(verbosity=2)
