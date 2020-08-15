import unittest
from app import getNextGap
from app import combSort

class TestCombSort(unittest.TestCase):
    def test_path_1(self):
        unsortedList = [3, 11, 5, 2]
        self.assertEqual(combSort(unsortedList), sorted(unsortedList, key=int))

    def test_path_2(self):
        sortedList = [1, 2, 3, 4]
        self.assertEqual(combSort(sortedList), sorted(sortedList, key=int))

    def test_path_3(self):
        negative_ghost_rider = []
        self.assertEqual(combSort(negative_ghost_rider), sorted(negative_ghost_rider, key=int))


