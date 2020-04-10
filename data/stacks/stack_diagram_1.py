"""
Pilha (Stack)
Pilha é uma estrutura de dados abstrata que segue o princípio LIFO (Last In
First Out) - último item a entrar, será o primeiro a sair.
A adição e remoção de novos itens ocorre sempre na mesma ponta. O final da
pilha, representa seu topo, o começo da pilha representa sua base.

Podemos usar listas para representar pilhas em Python já que só precisamos dos
métodos append, para adicionar itens ao topo da pilha e pop, para remover
itens do topo da pilha.

Exemplos abaixo são apenas para append
"""
from typing import List

stack: List[str] = []

stack.append('A')
stack.append('B')
stack.append('C')

print(stack)
