import unittest
import solution as s


class TestSolution(unittest.TestCase):

    def test_solution_reverse_vowels(self):
        res = s.reverse_vowels("hello")
        exp = "holle"
        self.assertEqual(res, exp)

        res = s.reverse_vowels("leetcode")
        exp = "leotcede"
        self.assertEqual(res, exp)

        res = s.reverse_vowels("aA")
        exp = "Aa"
        self.assertEqual(res, exp)

        res = s.reverse_vowels("race car")
        exp = "race car"
        self.assertEqual(res, exp)


if __name__ == "__main__":
    unittest.main()
