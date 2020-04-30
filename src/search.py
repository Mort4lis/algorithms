from typing import Any, List


def binary_search(arr: List[Any], item: Any) -> int:
    """
    Метод бинарного поиска.

    Находит индекс элемента с логарифмической временной сложностью O(log(n)).
    Алгоритм: Находим индекс центрального элемента, и сверяем значение по этому индексу
    с элементом, переданным в качестве аргумента `item`. В случае если два элемента равны, то
    возвращаем центральный индекс. Если же нет, то находим ту часть, в которой может быть потенциально
    найденный элемент (то есть, делим массив на две части и выбираем одну из двух половинок). И повторяем
    алгоритм до тех пор пока не останется один элемент.

    :param arr: Отсорированный массив элементов
    :param item: Искомый элемент
    :return: Возвращает индекс найденного элемента, либо -1 в случае отсутствия элемента в массиве
    """
    begin = 0
    end = len(arr) - 1

    while begin <= end:
        mid = (begin + end) // 2
        if arr[mid] == item:
            return mid
        if arr[mid] < item:
            begin = mid + 1
        else:
            end = mid - 1
    return -1


def recursive_binary_search(arr: List[Any], item: Any, begin=0, end=None) -> int:
    """
    Метод рекурсивного бинарного поиска.

    :param arr: Отсорированный массив элементов
    :param item: Искомый элемент
    :param begin: Начальный индекс рассматриваемой задачи
    :param end: Конечный индекс рассматриваемой задачи
    :return: Возвращает индекс найденного элемента, либо -1 в случае отсутствия элемента в массиве
    """
    end = len(arr) - 1 if end is None else end
    if begin >= end:
        return -1

    mid = (begin + end) // 2
    if arr[mid] == item:
        return mid

    if arr[mid] < item:
        return recursive_binary_search(arr, item, begin=mid + 1, end=end)
    return recursive_binary_search(arr, item, begin=begin, end=mid)
