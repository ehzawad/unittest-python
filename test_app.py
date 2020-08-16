import unittest
from app import combSort
import random


class TestCombSort_branch(unittest.TestCase):

    ## testcase for path coverage

    def test_path_04(self):
        l = [1]
        self.assertEqual(combSort(l), sorted(l, key=int))

    def test_path_02(self):
        sortedList = [1,4]
        self.assertEqual(combSort(sortedList), sorted(sortedList, key=int))

    def test_path_01(self):
        unsortedList = [3, 11, 5, 2]
        self.assertEqual(combSort(unsortedList), sorted(unsortedList, key=int))


class TestCombSort_Conditions(unittest.TestCase):

    def test_path_03(self):
        negative_ghost_rider = []
        self.assertEqual(combSort(negative_ghost_rider), sorted(negative_ghost_rider, key=int))

    def test_path_12(self):
        l = [3, 3]
        self.assertEqual(combSort(l), sorted(l, key=int))


class TestCombSort_loop_coverage(unittest.TestCase):

    def test_path_06(self):
        l = [8, 7]
        self.assertEqual(combSort(l), sorted(l, key=int))


    def test_path_forloop(self):
        #Generate 5 random numbers between 10 and 30
        randomlist = random.sample(range(10, 30), 5)
        self.assertEqual(combSort(randomlist), sorted(randomlist, key=int))


    def test_path_forloop(self):
        MAX = 100
        randomlist = random.sample(range(1, 1000), MAX)
        self.assertEqual(combSort(randomlist), sorted(randomlist, key=int))




