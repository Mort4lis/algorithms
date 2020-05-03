from typing import List, Any


def recursive_sum(arr: List[Any]) -> int:
    """
    Рекурсивная функция подсчета суммы элементов списка.

    Метод решения задачи основан на принципе "Разделяй и влавствуй".

    :param arr: Входной список элементов
    :return: Сумма элементов списка
    """
    if len(arr) == 0:
        return 0
    return arr[0] + recursive_sum(arr[1:])


def count(arr: List[Any]) -> int:
    """
    Рекурсивная функция подсчета количества элементов в списке.

    Метод решения задачи основан на принципе "Разделяй и влавствуй".

    :param arr: Входной список элементов
    :return: Количество элементов в списке
    """
    if not arr:
        return 0
    return 1 + count(arr[1:])


def max_element(arr: List[Any]) -> Any:
    """
    Рекурсивная функция поиска максимального элемента в списке.

    Метод решения задачи основан на принципе "Разделяй и влавствуй".

    :param arr: Входной список элементов
    :return: Максимальный элемент в списке
    """
    length = len(arr)
    if length == 0:
        raise ValueError('max_element() arg is an empty sequence')

    if length == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]

    sub_max = max_element(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max


def generate_bracket_sequences(n: int) -> List[str]:
    """
    Метод решения вывода всевозможных корректных скобочных последовательностей.

    :param n: Натуральное число
    :return: Список строк (скобочных последовательностей)
    """
    result = []
    total_seq_len = 2 * n

    def bypass(seq, now_open, was_open):
        current_len_seq = len(seq)
        if current_len_seq == total_seq_len:
            result.append(seq)
            return

        if was_open < n:
            bypass(seq + '(', now_open + 1, was_open + 1)
        if now_open >= 1:
            bypass(seq + ')', now_open - 1, was_open)

    bypass('(', 1, 1)
    return result
