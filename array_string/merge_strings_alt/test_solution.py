import unittest
import solution as s


class TestSolution(unittest.TestCase):

    def test_solution_merge_strings_alt(self):
        res = s.merge_strings_alt("abc", "pqr")
        exp = "apbqcr"
        self.assertEqual(res, exp)

        res = s.merge_strings_alt("ab", "pqrs")
        exp = "apbqrs"
        self.assertEqual(res, exp)

        res = s.merge_strings_alt("abcd", "pq")
        exp = "apbqcd"
        self.assertEqual(res, exp)


if __name__ == "__main__":
    unittest.main()
