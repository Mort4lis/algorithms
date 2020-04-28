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


def bubble_sort(arr: List[Any]) -> List[Any]:
    """
    Сортировка Пузырьков.

    Временная сложность: O(n^2)
    Алгоритм: Выполняем цикл до тех пор пока есть изменения (перестановки двух элементов местами).
    Берем первые два элемента, проверяем их: если элемент слева больше, чем элемент справа - меняем
    местами, если нет - пропускаем. Берем следующие два элемента и опять проверям их и т.д.

    :param arr: Исходный массив элементов
    :return: Отсортированный массив элементов
    """
    result = deepcopy(arr)
    length = len(result)
    has_changes = True

    while has_changes:
        has_changes = False
        for i in range(length - 1):
            if result[i] > result[i + 1]:
                result[i], result[i + 1] = result[i + 1], result[i]
                has_changes = True

    return result
