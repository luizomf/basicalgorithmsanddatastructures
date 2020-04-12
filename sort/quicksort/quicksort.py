"""
Quicksort algorithm

You may not need this in Python

>>> print(quicksort(list_of_numbers))
[2, 2, 4, 5, 9, 10, 11, 122, 123, 321]
>>> print(quicksort(list_of_words))
['Aline', 'Helena', 'João', 'Luiz', 'Maria', 'Zara']
>>> print(quicksort(['A']))
['A']
>>> print(quicksort(['B', 'A']))
['A', 'B']
>>> print(quicksort([]))
[]
"""

import doctest
from typing import List, TypeVar

TListValue = TypeVar('TListValue', int, float, str, bool)


list_of_numbers: List[int] = [10, 9, 5, 2, 11, 4, 2, 123, 321, 122]
list_of_words: List[str] = ['Luiz', 'Maria', 'João', 'Helena', 'Zara', 'Aline']


def quicksort(a_list: List[TListValue]) -> List[TListValue]:
    if len(a_list) < 2:
        return a_list

    pivot_index = len(a_list) // 2
    pivot = a_list.pop(pivot_index)
    smaller_values: List = [item for item in a_list if item <= pivot]
    higher_values: List = [item for item in a_list if item > pivot]

    return quicksort(smaller_values) + [pivot] + quicksort(higher_values)


if __name__ == "__main__":
    doctest.testmod(verbose=False)
