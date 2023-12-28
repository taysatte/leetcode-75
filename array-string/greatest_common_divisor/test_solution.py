import unittest
import solution as s


class TestSolution(unittest.TestCase):

    def test_solution_gcf_of_strings(self):
        res = s.gcd_of_strings("ABCABC", "ABC")
        exp = "ABC"
        self.assertEqual(res, exp)

        res = s.gcd_of_strings("ABABAB", "ABAB")
        exp = "AB"
        self.assertEqual(res, exp)

        res = s.gcd_of_strings("LEET", "CODE")
        exp = ""
        self.assertEqual(res, exp)


if __name__ == "__main__":
    unittest.main()
