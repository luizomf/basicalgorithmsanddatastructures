import unittest
from sort.quicksort.quicksort import quicksort
from typing import List


class QuicksortTest(unittest.TestCase):
    def setUp(self):
        # Default values
        self.list_of_numbers: List[int] = [
            10, 9, 5, 2, 11, 4, 2, 123, 321, 122
        ]
        self.list_of_words: List[str] = [
            'Luiz', 'Maria', 'João', 'Helena', 'Zara', 'Aline'
        ]

    def test_quicksort_numbers(self):
        self.assertEqual(
            quicksort(self.list_of_numbers),
            [2, 2, 4, 5, 9, 10, 11, 122, 123, 321]
        )

    def test_quicksort_words(self):
        self.assertEqual(
            quicksort(self.list_of_words),
            ['Aline', 'Helena', 'João', 'Luiz', 'Maria', 'Zara']
        )
