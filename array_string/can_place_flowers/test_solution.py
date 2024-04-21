import unittest
import solution as s


class TestSolution(unittest.TestCase):

    def test_solution_can_place_flowers(self):
        res = s.can_place_flowers([1, 0, 0, 0, 1], 1)
        self.assertTrue(res)

        res = s.can_place_flowers([1, 0, 0, 0, 1], 2)
        self.assertFalse(res)

        res = s.can_place_flowers([0, 0, 1, 0, 1], 1)
        self.assertTrue(res)


if __name__ == "__main__":
    unittest.main()
