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
