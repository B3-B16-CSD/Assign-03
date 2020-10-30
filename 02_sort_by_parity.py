# pylint: disable=invalid-name
"""
Sort by parity
Given a list of strings lst and a list of integers p,
reorder lst so that every lst[i] gets placed to p[i].

Example 1
Input
lst = ["a", "b", "c", "d"]
p = [3, 0, 1, 2]

Output
["b", "c", "d", "a"]

Explanation
a goes to index 3
b goes to index 0
c goes to index 1
d goes to index 2
"""


import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput


def sort_by_parity(lst, p):
 


# DO NOT TOUCH THE BELOW CODE
# pylint: disable=unused-variable,line-too-long
class TestSortByParity(unittest.TestCase):

    def test_01(self):
        self.assertEqual(sort_by_parity(["a", "b", "c", "d"],
                                        [3, 0, 1, 2]), ["b", "c", "d", "a"])

    def test_02(self):
        self.assertEqual(sort_by_parity([], []), [])

    def test_03(self):
        self.assertEqual(sort_by_parity(["z"], [0]), ["z"])

    def test_04(self):
        self.assertEqual(sort_by_parity(["yxfnqespg", "zuodgmgt", "elt", "lmueb", "ht", "tnlbb", "stqxxo", "bwtlooy", "grhoegece"],
                                        [6, 2, 1, 0, 5, 7, 8, 3, 4]),
                         ["lmueb", "elt", "zuodgmgt", "bwtlooy", "grhoegece", "ht", "yxfnqespg", "tnlbb", "stqxxo"])

    def test_05(self):
        self.assertEqual(sort_by_parity(["gzn", "kbuxe", "kmmvafrxvp", "pfpdlq", "idzttxo", "zjefnzeelx", "nqsj", "rps", "vabsi", "suuqszu"],
                                        [2, 8, 3, 1, 7, 9, 0, 4, 5, 6]),
                         ["nqsj", "pfpdlq", "gzn", "kmmvafrxvp", "rps", "vabsi", "suuqszu", "idzttxo", "kbuxe", "zjefnzeelx"])

    def test_06(self):
        self.assertEqual(sort_by_parity(["ufjd", "cp", "tdapigcss", "vpqomb", "diok", "uv", "heiwbffj", "kwovtsi", "oecu", "tza", "wz", "fpceonw"],
                                        [1, 4, 0, 11, 10, 7, 3, 5, 6, 9, 8, 2]),
                         ["tdapigcss", "ufjd", "fpceonw", "heiwbffj", "cp", "kwovtsi", "oecu", "uv", "wz", "tza", "diok", "vpqomb"])


if __name__ == '__main__':
    unittest.main(verbosity=2)
