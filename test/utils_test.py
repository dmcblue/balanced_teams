import unittest
import logging
from balance.utils import list_intersection

class ListIntersectionTest:
    def __init__(self, a, b, expected):
        self.a = a
        self.b = b
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


if __name__ == '__main__':
    unittest.main()
