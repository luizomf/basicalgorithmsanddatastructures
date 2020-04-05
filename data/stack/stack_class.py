# append, pop, peek
# iterar com for e com while

from __future__ import annotations
from typing import List, Any
from copy import deepcopy


class Stack:
    def __init__(self) -> None:
        self.__data: List[Any] = []
        self.__index = 0

    def append(self, item: Any) -> None:
        self.__data.append(item)

    def pop(self) -> Any:
        return self.__data.pop()

    def peek(self) -> Any:
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


if __name__ == "__main__":
    stack = Stack()

    stack.append('A')
    stack.append('B')
    stack.append('C')

    print('FOR:')
    for item in stack:
        print(item)

    stack_copy = deepcopy(stack)
    print('\nWHILE:')
    while stack_copy:
        print(stack_copy.pop())

    stack_copy = deepcopy(stack)
    print('\nWHILE:')
    while stack_copy:
        print(stack_copy.pop())

    stack_copy = deepcopy(stack)
    print('\nWHILE:')
    while stack_copy:
        print(stack_copy.pop())

    print('\nStack original:', stack)
