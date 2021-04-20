import unittest
import logging
from balance.utils import list_intersection, \
                          list_partition

class ListIntersectionTest:
    def __init__(self, a, b, expected):
        self.a = a
        self.b = b
        self.expected = expected

class ListPartitionTest:
    def __init__(self, lst, parts, expected):
        self.lst = lst
        self.parts = parts
        self.expected = expected

class TestUtils(unittest.TestCase):

    def test_list_intersection(self):
        tests = [
            ListIntersectionTest(
                ['a', 'b'],
                ['b', 'c'],
                ['b']
            ),
            ListIntersectionTest(
                ['a', 'b', 'c'],
                ['b', 'c', 'd'],
                ['b', 'c']
            ),
            ListIntersectionTest(
                ['a', 'b'],
                ['c', 'd'],
                []
            )
        ]
        for test in tests:
            self.assertEqual(
                set(test.expected),
                set(list_intersection(test.a, test.b))
            )

    def test_list_partition(self):
        tests = [
            ListPartitionTest(
                ['a', 'b', 'c', 'd'],
                2,
                [['a', 'b'], ['c', 'd']]
            ),
            ListPartitionTest(
                ['a', 'b', 'c', 'd', 'e'],
                2,
                [['a', 'b', 'c'], ['d', 'e']]
            ),
            ListPartitionTest(
                ['a', 'b', 'c', 'd', 'e'],
                3,
                [['a', 'b'], ['c', 'd'], ['e']]
            )
        ]
        for test in tests:
            parts = list(list_partition(test.lst, test.parts))
            self.assertEqual(len(test.expected), len(parts))
            for index in range(0, len(parts)):
                self.assertEqual(
                    test.expected[index],
                    parts[index]
                )

if __name__ == '__main__':
    unittest.main()
