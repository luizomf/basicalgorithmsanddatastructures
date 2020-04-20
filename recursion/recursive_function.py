"""
Recursive functions

You may use for for better performance.

Read more about it in:
http://neopythonic.blogspot.com/2009/04/tail-recursion-elimination.html
"""

from typing import List


class Box:
    """A box that can or cannot have a key"""

    def __init__(self, name: str, has_key=False) -> None:
        self.name = name
        self.has_key = has_key

    def __repr__(self) -> str:
        return f'Box(name={self.name}, has_key={self.has_key})'


def open_boxes(list_of_boxes: List[Box], index: int = 0) -> Box:
    """A recursive function

    Args:
        list_of_boxes (List[Box]): A list of boxes
        index (int, optional): Actual index. Defaults to 0.

    Returns:
        Box: A box that has_key or a new empty Box
    """
    if index >= len(list_of_boxes):
        return Box('Empty box')

    box = list_of_boxes[index]

    print(f'Checking box of index {index} -> {box}')

    if list_of_boxes[index].has_key:
        print(f'Returning index box index {index} -> {box}')
        return box
    else:
        index += 1
        return open_boxes(list_of_boxes, index)


if __name__ == "__main__":
    boxes: List[Box] = [
        Box(name='Product Box'), Box(name='Clothing box'),
        Box(name='Items box', has_key=True), Box(name='Books Box'),
        Box(name='Paper box'), Box(name='Tool box')
    ]

    print(open_boxes(boxes))
