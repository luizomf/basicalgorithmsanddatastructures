"""
Uma classe que representa uma stack.

Podemos criar uma classe para representação de uma stack. Isso nos permite
expor apenas os métodos que queremos, da maneira que desejarmos.

Por exemplo: na classe a seguir, vamos expor apenas os métodos append, pop (sem
permitir índice) e peek (o mesmo que pop, mas sem eliminar o topo da pilha).

Também implementamos os métodos dunder a seguir:
    - __repr__: para representação da classe
    - __iter__ e __next__: para iteração com for
    - __bool__: para iteração com while. O método __bool__ retorna True se
    nossa stack tiver valores e False se não.
"""

from __future__ import annotations
from typing import List, Any


class Stack:
    """Classe representando uma stack"""

    def __init__(self) -> None:
        # Representa os itens da nossa stack
        self.__data: List[Any] = []
        # Representa o índice para iterações com for
        self.__index = 0

    def append(self, item: Any) -> None:
        """Este método repassa as informações para append da lista original"""
        self.__index += 1
        self.__data.append(item)

    def pop(self) -> Any:
        """O mesmo que pop, porém sem aceitar índice"""
        return self.__data.pop()

    def peek(self) -> Any:
        """O mesmo que pop, sem eliminar o topo da pilha"""
        if not self.__data:
            return []

        return self.__data[-1]

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.__data})'

    def __iter__(self) -> Stack:
        self.__index = len(self.__data)
        return self

    def __next__(self) -> Any:
        if self.__index == 0:
            raise StopIteration

        self.__index -= 1
        return self.__data[self.__index]

    def __bool__(self) -> bool:
        return bool(self.__data)


# if __name__ == "__main__":
    # stack = Stack()

    # stack.append('A')
    # stack.append('B')
    # stack.append('C')

    # print('FOR:')
    # for item in stack:
    #     print(item)

    # stack_copy = deepcopy(stack)
    # print('\nWHILE:')
    # while stack_copy:
    #     print(stack_copy.pop())

    # stack_copy = deepcopy(stack)
    # print('\nWHILE:')
    # while stack_copy:
    #     print(stack_copy.pop())

    # stack_copy = deepcopy(stack)
    # print('\nWHILE:')
    # while stack_copy:
    #     print(stack_copy.pop())

    # print('\nStack original:', stack)
