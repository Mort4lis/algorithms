from typing import Any, List

import pytest

from src.recursive import recursive_sum, count

test_data = [
    [],
    [4, 2, 1, 6, 0],
    [-1, 4, -100, 42, 5, 1],
    [10, 10, 0],
    [0, 0, 0]
]


@pytest.mark.parametrize('arr', test_data)
def test_recursive_sum(arr: List[Any]) -> None:
    """
    Тестирование рекурсивного метода подсчета суммы элементов.

    :param arr: Входной массив элементов
    """
    assert recursive_sum(arr) == sum(arr)


@pytest.mark.parametrize('arr', test_data)
def test_count(arr: List[Any]) -> None:
    """
    Тестирование рекурсивного метода подсчета количества элементов в списке.

    :param arr: Входной массив элементов
    """
    assert count(arr) == len(arr)
