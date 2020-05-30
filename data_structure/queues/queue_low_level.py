from __future__ import annotations
from typing import Any

EMPTY_NODE_VALUE = '__EMPTY_NODE__'


class EmptyQueueError(Exception):
    ...


class Node:
    def __init__(self, value: Any) -> None:
        self.value: Any = value
        self.next: Node

    def __repr__(self) -> str:
        return f'{self.value}'

    def __bool__(self) -> bool:
        return bool(self.value != EMPTY_NODE_VALUE)


class Queue:
    def __init__(self) -> None:
        self.first: Node = Node(EMPTY_NODE_VALUE)
        self.last: Node = Node(EMPTY_NODE_VALUE)
        self._count = 0

    def push(self, nodeValue: Any) -> None:
        new_node = Node(nodeValue)

        if not self.last:
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node

        if not self.first:
            self.first = new_node

        self._count += 1

    def pop(self) -> Node:
        if not self.first:
            raise EmptyQueueError('Empty queue')

        first = self.first

        if hasattr(self.first, 'next'):
            self.first = self.first.next
        else:
            self.first = Node(EMPTY_NODE_VALUE)

        self._count -= 1
        return first

    def peek(self) -> Node:
        return self.first

    def __len__(self) -> int:
        return self._count

    def __bool__(self) -> bool:
        return bool(self._count)

    def __iter__(self) -> Queue:
        return self

    def __next__(self) -> Any:
        try:
            next_value = self.pop()
            return next_value
        except EmptyQueueError:
            raise StopIteration


if __name__ == "__main__":
    queue = Queue()
    queue.push('A')
    queue.push('B')
    queue.push('C')
    queue.push('D')

    print(len(queue))

    print('Fora do for', next(queue))

    for item in queue:
        print(item, len(queue))
