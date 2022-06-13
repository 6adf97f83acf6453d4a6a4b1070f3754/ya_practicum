import random
import time
from typing import List


def remove_zeroes(nums: List[int]) -> None:
    """
    Удаляет все нули из массива. Сложность - O(n) для перемещения всех нулей в конец массива
    (будут пройдены все элементы), затем O(m) для удаления нулей (m - количество нулей)

    Дополнительная память не используется, все операции проводятся с изначальным массивом
    :param nums: массив чисел
    :return: меняет массив, ничего не возвращает
    """
    last_non_zero = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[last_non_zero] = nums[last_non_zero], nums[i]
            last_non_zero += 1

    for i in range(last_non_zero, len(nums)):
        nums.pop()


class Timer:
    def __init__(self):
        self.start = 0

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('{:.4e}'.format(time.time() - self.start))


if __name__ == '__main__':
    l = [0, 0, 2, 0, 1]
    remove_zeroes(l)
    assert l == [2, 1]

    l = [10, 20, 2, 30, 1]
    remove_zeroes(l)
    assert l == [10, 20, 2, 30, 1]

    l = [random.randint(0, 20) for i in range(1_000)]
    with Timer():
        remove_zeroes(l)

    l = [random.randint(0, 20) for i in range(10_000)]
    with Timer():
        remove_zeroes(l)

