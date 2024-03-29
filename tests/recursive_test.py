from typing import Any, List

import pytest

from src.recursive import recursive_sum, count, max_element, generate_bracket_sequences

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

    :param arr: Входной список элементов
    """
    assert recursive_sum(arr) == sum(arr)


@pytest.mark.parametrize('arr', test_data)
def test_count(arr: List[Any]) -> None:
    """
    Тестирование рекурсивного метода подсчета количества элементов в списке.

    :param arr: Входной список элементов
    """
    assert count(arr) == len(arr)


@pytest.mark.parametrize('arr', test_data)
def test_max_element(arr: List[Any]) -> None:
    """
    Тестирование рекурсивного метода поиска максимального элемента в списке.

    :param arr: Входной список элементов
    """
    if len(arr) == 0:
        with pytest.raises(ValueError):
            assert max_element(arr)
    else:
        assert max_element(arr) == max(arr)


@pytest.mark.parametrize(['n', 'result'], [
    (1, ['()']),
    (2, [
        '()()',
        '(())'
    ]),
    (3, [
        '()()()',
        '()(())',
        '(())()',
        '((()))',
        '(()())'
    ])
])
def test_generate_bracket_sequences(n, result) -> None:
    """
    Тестирование метода вывода списка корректных скобочных последовательностей.

    :param n: Натуральное число
    :param result: Список корректных скобочных последовательностей
    """
    seqs = generate_bracket_sequences(n)
    assert set(seqs) == set(result)
