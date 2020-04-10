"""
IndexError quando a pilha está vazia.

Quando os elementos da pilha forem esgotados e sua pilha ficar vazia, ao chamar
o método pop, teremos uma exceção (um erro) de IndexError.

Podemos tratá-lo com blocos try/except.
"""

from typing import List

# Uma pilha vazia
stack: List[str] = []

# Adicionando elementos no topo da pilha
stack.append('A')
stack.append('B')
stack.append('C')

# Blocos try/catch para evitar que uma exceção estoure
# quando a pilha estiver vazia
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
