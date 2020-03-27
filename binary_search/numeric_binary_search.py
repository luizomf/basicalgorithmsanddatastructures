"""
This is for studies only

You can use this instead of binary search:
>>> my_list = [0, 1, 2, 3]
>>> try:
...     index = my_list.index(10)
... except ValueError:
...     index = -1
>>> print(index)  # -1
-1

Tests:
>>> my_list = [0, 1, 2, 3]
>>> numeric_binary_search(my_list, 0)
0

>>> numeric_binary_search(my_list, 1)
1

>>> numeric_binary_search(my_list, 2)
2

>>> numeric_binary_search(my_list, 3)
3

>>> numeric_binary_search(my_list, 4)
-1

>>> numeric_binary_search(1, 4)
Traceback (most recent call last):
...
AssertionError: ordered_numbers Must be a list

>>> numeric_binary_search(my_list, '4')
Traceback (most recent call last):
...
AssertionError: Search must be int
"""

import doctest
from typing import List


def numeric_binary_search(ordered_numbers: List[int], search: int) -> int:
    """Simple numeric binary search

    Args:
        ordered_numbers(List[int]): an ordered list of numbers
        search(int): number to find

    Returns:
        int: found index or -1
    """
    assert isinstance(ordered_numbers, list), 'ordered_numbers Must be a list'
    assert isinstance(search, int), 'Search must be int'

    lowest_index = 0
    highest_index = len(ordered_numbers) - 1
    intermediate_index = highest_index // 2

    while lowest_index <= highest_index:
        actual_value = ordered_numbers[intermediate_index]

        if actual_value == search:
            return intermediate_index

        if actual_value < search:
            lowest_index = intermediate_index + 1

        if actual_value > search:
            highest_index = intermediate_index - 1

        intermediate_index = (highest_index + lowest_index) // 2

    return -1


if __name__ == "__main__":
    doctest.testmod(verbose=True)
