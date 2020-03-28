"""
Linear Search O(n)
"""
import re
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
    for person in people_names:
        firstname, lastname = person.values()

        if name_to_find == f'{firstname} {lastname}':
            return person

        regex = re.compile(fr'{firstname}\s+{lastname}', flags=re.I)
        if regex.search(name_to_find):
            return person

    return {}


if __name__ == "__main__":
    person_1 = person_name_search(people_names, 'helena  Oliveira')
    person_2 = person_name_search(people_names, 'João barbosa')

    print(person_1)
    print(person_2)
