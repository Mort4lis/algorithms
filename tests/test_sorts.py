from copy import deepcopy
from typing import Any, List

import pytest

from src.sorts import bubble_sort, insertion_sort, quick_sort, selection_sort

test_data = [
    [5, 1, 3, 2, 6, 4],
    [1, 5, 2, 6, 0, -10, -4, -3],
    [],
    [0, 0, 0],
    [-10, -100, -54, -12],
    [-1, -1, -1]
]


@pytest.mark.parametrize('arr', test_data)
def test_selection_sort(arr: List[Any]):
    """
    Тестирование метода сортировки Выбором.

    Проверяет также на неизменность исходного массива.

    :param arr: Исходный массив элементов
    """
    dump = deepcopy(arr)
    assert selection_sort(arr) == sorted(arr)
    assert arr == dump


@pytest.mark.parametrize('arr', test_data)
def test_bubble_sort(arr: List[Any]) -> None:
    """
    Тестирование метода сортировки Пузырьком.

    Проверяет также на неизменность исходного массива.

    :param arr: Исходный массив элементов
    """
    dump = deepcopy(arr)
    assert bubble_sort(arr) == sorted(arr)
    assert arr == dump


@pytest.mark.parametrize('arr', test_data)
def test_insertion_sort(arr: List[Any]) -> None:
    """
    Тестирование метода сортировки Вставками.

    Проверяет также на неизменность исходного массива.

    :param arr: Исходный массив элементов
    """
    dump = deepcopy(arr)
    assert insertion_sort(arr) == sorted(arr)
    assert arr == dump


@pytest.mark.parametrize('arr', test_data)
def test_quick_sort(arr: List[Any]) -> None:
    """
    Тестирование метода Быстрой сортировки.

    Проверяет также на неизменность исходного массива.

    :param arr: Исходный массив элементов
    """
    dump = deepcopy(arr)
    assert quick_sort(arr) == sorted(arr)
    assert arr == dump
