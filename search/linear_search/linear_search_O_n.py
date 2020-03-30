"""
Linear Search on List[Dict[str, str]] O(n)

Tests:
>>> person_name_search(people_names, 'Luiz')
{}

>>> person_name_search(people_names, 'Luiz Miranda')
{'firstname': 'Luiz', 'lastname': 'Miranda'}

>>> person_name_search(people_names, 'luiz  miranda')
{'firstname': 'Luiz', 'lastname': 'Miranda'}
"""
import re
import doctest
from typing import List, Dict

people_names: List[Dict[str, str]] = [
    {'firstname': 'Luiz', 'lastname': 'Miranda'},
    {'firstname': 'Maria', 'lastname': 'Moreira'},
    {'firstname': 'Elaine', 'lastname': 'Figueiredo'},
    {'firstname': 'Helena', 'lastname': 'Oliveira'},
    {'firstname': 'vivian', 'lastname': 'Silva'},
    {'firstname': 'Fabrício', 'lastname': 'Costa'},
    {'firstname': 'Eduardo', 'lastname': 'Vieira'},
    {'firstname': 'Lívia', 'lastname': 'Madeira'},
    {'firstname': 'João', 'lastname': 'Barbosa'},
    {'firstname': 'Dania', 'lastname': 'Maia'},
]


def person_name_search(
    people_names: List[Dict[str, str]], name_to_find: str
) -> Dict[str, str]:
    """A linear search on List[Dict['firstname', 'lastname']]

    Args:
        people_names (List[Dict[str, str]]): A list of dicts with names.
            Dict keys must include first and lastname as first and second keys.
        name_to_find (str): [description]: A name to find

    Returns:
        Dict[str, str]: The dict with firstname and lastname of empty dict
    """
    for person in people_names:
        firstname, lastname, *_ = person.values()

        if name_to_find == f'{firstname} {lastname}':
            return person

        regex = re.compile(fr'{firstname}\s+{lastname}', flags=re.I)
        if regex.search(name_to_find):
            return person

    return {}


if __name__ == "__main__":
    doctest.testmod(verbose=True)
    # person_1 = person_name_search(people_names, 'helena  Oliveira')
    # person_2 = person_name_search(people_names, 'João barbosa')

    # print(person_1)
    # print(person_2)
