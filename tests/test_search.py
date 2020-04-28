import pytest
from typing import List, Any

from src.search import binary_search


@pytest.mark.parametrize(['arr', 'item', 'result'], [
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], 8, 7),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], 11, -1),
    ([], 10, -1),
    ([-5, -3, 5, 10, 15], -3, 1),
    ([1, 3, 5, 7, 9], 3, 1),
    ([1, 3, 5, 7, 9], -1, -1)
])
def test_binary_search(arr: List[Any], item: Any, result: int) -> None:
    """
    Тестирование метода Бинарного поиска.

    :param arr: Отсорированный массив элементов
    :param item: Искомый элемент
    :param result: Индекс искомого элемента
    """
    assert binary_search(arr, item) == result
