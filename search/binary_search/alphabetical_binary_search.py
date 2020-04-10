"""
This is for studies only

You can use this instead of binary search:
>>> try:
...     index = sorted_names.index('Aaren')
... except ValueError:
...     index = -1
>>> print(index)
0

Tests for the function:
>>> alphabetical_binary_search(sorted_names, 'Zorine')
915

>>> alphabetical_binary_search(sorted_names, 'Zuzana')
919

>>> alphabetical_binary_search(sorted_names, 'Aaren')
0

>>> alphabetical_binary_search(sorted_names, 'Otávio')
-1
"""
try:
    import sys
    import os

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../../'
            )
        )
    )
except ImportError:
    raise

import doctest
from typing import List
# ../../data
from data_structure.sorted_names import sorted_names


def alphabetical_binary_search(sorted_list: List, search_name: str) -> int:
    """Alphabetical binary search (for study purpuses)

    Args:
        sorted_list (List): A list of names (must be ordered)
        search_name (str): name to search

    Returns:
        int: found index or -1
    """
    lowest_index = 0
    highest_index = len(sorted_list) - 1
    intermediate_index = highest_index // 2

    while lowest_index <= highest_index:
        name = sorted_list[intermediate_index]

        if search_name == name:
            return intermediate_index

        if name > search_name:
            highest_index = intermediate_index - 1

        if name < search_name:
            lowest_index = intermediate_index + 1

        intermediate_index = (lowest_index + highest_index) // 2

    return -1


if __name__ == "__main__":
    doctest.testmod(verbose=True)
    alphabetical_binary_search(sorted_names, 'Karoline')
