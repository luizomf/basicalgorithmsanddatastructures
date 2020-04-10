"""
Como falamos em listas, podemos fazer iterações na pilha normalmente, tanto com
while quanto com for.
"""

from typing import List
from copy import deepcopy

# Uma pilha vazia
stack: List[List[str]] = []

# Append adiciona elementos no topo da pilha
stack.append(['A'])
stack.append(['B'])
stack.append(['C'])

# Iteração com for (sem mutações)
print('FOR:')
for item in stack[::-1]:
    print(item)

# Podemos iterar com while (com mutação). O ideal aqui
# será copiar a pilha original para evitar mutações
# na mesma.
stack_copy = deepcopy(stack)

# Iteração com while mutando os valores (esgotando a pilha)
print('\nWHILE:')
while stack_copy:
    item = stack_copy.pop()
    item += ['Manipulei']
    print(item)

# A pilha original continua intacta
print('\nSUA PILHA:', stack)
