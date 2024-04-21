import unittest
import solution as s


class TestSolution(unittest.TestCase):

    def test_solution_kids_with_candies(self):
        res = s.kids_with_candies([2, 3, 5, 1, 3], 3)
        exp = [True, True, True, False, True]
        self.assertEqual(res, exp)

        res = s.kids_with_candies([4, 2, 1, 1, 2], 1)
        exp = [True, False, False, False, False]
        self.assertEqual(res, exp)

        res = s.kids_with_candies([12, 1, 12], 10)
        exp = [True, False, True]
        self.assertEqual(res, exp)


if __name__ == "__main__":
    unittest.main()
