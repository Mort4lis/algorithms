from typing import List, Any


def recursive_sum(arr: List[Any]) -> int:
    """
    Рекурсивная функция подсчета суммы элементов списка.

    Метод решения задачи основан на принципе "Разделяй и влавствуй".

    :param arr: Входной массив элементов
    :return: Сумма элементов списка
    """
    if len(arr) == 0:
        return 0
    return arr[0] + recursive_sum(arr[1:])


def count(arr: List[Any]) -> int:
    """
    Рекурсивная функция подсчета количества элементов в списке.

    Метод решения задачи основан на принципе "Разделяй и влавствуй".

    :param arr: Входной массив элементов
    :return: Количество элементов в списке
    """
    if not arr:
        return 0
    return 1 + count(arr[1:])


def max_element(arr: List[Any]) -> Any:
    """
    Рекурсивная функция поиска максимального элемента в списке.

    Метод решения задачи основан на принципе "Разделяй и влавствуй".

    :param arr: Входной массив элементов
    :return: Максимальный элемент в списке
    """
    length = len(arr)
    if length == 0:
        raise ValueError('max_element() arg is an empty sequence')

    if length == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]

    sub_max = max_element(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max
