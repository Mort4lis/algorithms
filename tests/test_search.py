from typing import Any, List

import pytest
from pytest import fixture

from src.graphs import Node
from src.search import binary_search, recursive_binary_search, breadth_first_search, depth_first_search

test_data = [
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], 8),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], 11),
    ([], 10),
    ([-5, -3, 5, 10, 15], -3),
    ([1, 3, 5, 7, 9], 3),
    ([1, 3, 5, 7, 9], -1)
]


@pytest.mark.parametrize(['arr', 'item'], test_data)
def test_binary_search(arr: List[Any], item: Any) -> None:
    """
    Тестирование метода Бинарного поиска.

    :param arr: Отсорированный массив элементов
    :param item: Искомый элемент
    """
    try:
        index = arr.index(item)
    except ValueError:
        index = -1
    assert binary_search(arr, item) == index


@pytest.mark.parametrize(['arr', 'item'], test_data)
def test_recursive_binary_search(arr: List[Any], item: Any) -> None:
    """
    Тестирование метода Рекурсивного Бинарного поиска.

    :param arr: Отсорированный массив элементов
    :param item: Искомый элемент
    """
    try:
        index = arr.index(item)
    except ValueError:
        index = -1
    assert recursive_binary_search(arr, item) == index


@fixture(scope='module')
def graph():
    root = Node(1)
    root.children = [Node(2), Node(7), Node(8)]
    root.children[0].children = [Node(3), Node(6)]
    root.children[0].children[0].children = [Node(4), Node(5)]
    root.children[2].children = [Node(9), Node(12)]
    root.children[2].children[0].children = [Node(10), Node(11)]
    return root


@pytest.mark.parametrize(['value', 'result'], [
    (4, 3),
    (9, 2),
    (8, 1),
    (15, -1)
])
def test_breadth_first_search(graph, value, result) -> None:
    """
    Тестирование метода поиска в Ширину.

    :param graph: Фикстура проверяемого графа
    :param value: Искомое значение
    :param result: Результирующая (корректная) длина кратчайшего пути
    """
    assert breadth_first_search(graph, value) == result


@pytest.mark.parametrize(['value', 'result'], [
    (4, 3),
    (9, 2),
    (8, 1),
    (15, -1)
])
def test_depth_first_search(graph, value, result) -> None:
    """
    Тестирование метода поиска в Глубину.

    :param graph: Фикстура проверяемого графа
    :param value: Искомое значение
    :param result: Результирующая (корректная) длина кратчайшего пути
    """
    assert depth_first_search(graph, value) == result
