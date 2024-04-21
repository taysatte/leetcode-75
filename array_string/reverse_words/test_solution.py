import unittest
import solution as s


class TestSolution(unittest.TestCase):

    def test_solution_reverse_words(self):
        res = s.reverse_words("the sky is blue")
        exp = "blue is sky the"
        self.assertEqual(res, exp)

        res = s.reverse_words("  hello world  ")
        exp = "world hello"
        self.assertEqual(res, exp)

        res = s.reverse_words("a good   example")
        exp = "example good a"
        self.assertEqual(res, exp)


if __name__ == "__main__":
    unittest.main()
