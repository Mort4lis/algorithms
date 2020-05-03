from typing import Any, List


class Node:
    def __init__(self, value: Any) -> None:
        self._value = value
        self._children: List[Node] = []

    @property
    def children(self) -> List['Node']:
        return self._children

    @children.setter
    def children(self, nodes: List['Node']) -> None:
        self._children = nodes

    @property
    def value(self) -> Any:
        return self._value

    def __hash__(self):
        return id(self)
