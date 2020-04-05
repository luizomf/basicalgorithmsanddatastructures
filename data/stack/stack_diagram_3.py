"""
Iterações e cópia
"""

from typing import List
from copy import deepcopy

stack: List[List[str]] = []

stack.append(['A'])
stack.append(['B'])
stack.append(['C'])

print('FOR:')
for item in stack[::-1]:
    print(item)

stack_copy = deepcopy(stack)

print('\nWHILE:')
while stack_copy:
    item = stack_copy.pop()
    item += ['Manipulei']
    print(item)

print('\nSUA PILHA:', stack)
