"""
Podemos usar listas como "filas" (uma outra estrutura de dados abstrata),
porém não é recomendável. O custo de uma alteração no início da lista (base
da pilha) é linear - Complexidade de tempo linear, ou O(n), significa que
se eu remover o índice 0 da minha lista, todos os outros itens serão afetados.
"""

from typing import List

# Uma pilha vazia
stack: List[str] = []

# Adicionando itens no topo da pilha
stack.append('A')
stack.append('B')
stack.append('C')

# Removendo itens da base da pilha (comportamento não desejável)
# NÃO FAÇA ISSO.
first_item = stack.pop(0)

print(stack, first_item)
