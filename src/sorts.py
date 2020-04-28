from copy import deepcopy
from typing import Any, List


def selection_sort(arr: List[Any]) -> List[Any]:
    """
    Сортировка Выбором.

    Временная сложность: O(n^2)
    Алгоритм: На каждой итерации массива находим минимальный элемент и его индекс.
    Из исходного массива вырываем этот минимальный элемент (по индексу) и вставляем его
    в конец результирующего массива.

    :param arr: Исходный массив элементов
    :return: Отсортированный массив элементов
    """
    result = []
    arr_copy = deepcopy(arr)
    for _ in range(len(arr)):
        index = arr_copy.index(min(arr_copy))  # Находим индекс, чей элемент - минимален
        item = arr_copy.pop(index)
        result.append(item)
    return result
