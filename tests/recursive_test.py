import pytest
from typing import List, Any
from src.recursive import recursive_sum


@pytest.mark.parametrize('arr', [
    [],
    [4, 2, 1, 6, 0],
    [-1, 4, -100, 42, 5, 1],
    [10, 10, 0],
    [0, 0, 0]
])
def test_recursive_sum(arr: List[Any]) -> None:
    """
    Тестирование рекурсивного метода подсчета суммы элементов.

    :param arr: Входной массив элементов
    """
    assert recursive_sum(arr) == sum(arr)
