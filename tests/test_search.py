from typing import Any, List

import pytest

from src.search import binary_search, recursive_binary_search

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
