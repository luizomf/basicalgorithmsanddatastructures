"""
IndexError quando a pilha está vazia
"""

from typing import List

stack: List[str] = []

stack.append('A')
stack.append('B')
stack.append('C')

try:
    top_item = stack.pop()  # C
    print(stack, top_item)
    top_item = stack.pop()  # B
    print(stack, top_item)
    top_item = stack.pop()  # A
    print(stack, top_item)
    top_item = stack.pop()  # IndexError
    print(stack, top_item)
except IndexError:
    print('Pilha está vazia')
