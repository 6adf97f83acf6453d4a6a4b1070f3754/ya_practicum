import random
import time
from typing import List


def get_unique_elements(list_1: List, list_2: List) -> List:
    """
    Возвращает список элементов, которые есть в первом списке, но нет во втором

    Вычислительная сложность - O(m) для составления сета, O(n) для перебора элементов
    первого списка, проверка на вхождение - O(1) итого O(m + n), где m, n - размеры списков

    Память - O(n) - дополнительный массив размера не более n

    :param list_1: первый список
    :param list_2: второй список
    :return: список элементов, которые есть в первом списке, но нет во втором
    """
    second_set = set(list_2)
    result = []

    for el in list_1:
        if el not in second_set:
            result.append(el)

    return result


class Timer:
    def __init__(self):
        self.start = 0

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('{:.4e}'.format(time.time() - self.start))


if __name__ == '__main__':
    assert get_unique_elements([], [1, 2, 3]) == []
    assert get_unique_elements([1, 2, 3], []) == [1, 2, 3]
    assert get_unique_elements([1, 2, 3], [4, 5, 6]) == [1, 2, 3]
    assert get_unique_elements([1, 2, 3], [1, 2, 3]) == []

    l1 = [random.randint(0, 10_000) for i in range(10_000)]
    l2 = [random.randint(0, 10_000) for i in range(10_000)]
    with Timer():
        l3 = get_unique_elements(l1, l2)

    assert set(l2) - set(l3) == set(l2)

    l1 = [random.randint(0, 100_000) for i in range(100_000)]
    l2 = [random.randint(0, 100_000) for i in range(100_000)]
    with Timer():
        l3 = get_unique_elements(l1, l2)

    assert set(l2) - set(l3) == set(l2)