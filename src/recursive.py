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
