from inverse_element import inverse_element
import sys
from functools import reduce
from operator import mul


def chiness(matrix):
    a_array, m_array = list(map(list, zip(*matrix)))

    M = reduce(mul, m_array)

    res = 0
    for a, m in zip(a_array, m_array):
        m_i = M // m

        inv = inverse_element(m_i, m)
        if inv is None:
            return None

        res += a * m_i * inv

    return res % M, M


if __name__ == '__main__':
    print('''Введите коэффициенты системы сравнений (ctrl+D для завершения ввода):
Пример:
    2 5
    5 8
    2 3
Эквивалентно
    x = 2 (mod 5)
    x = 5 (mod 8)
    x = 2 (mod 3)
    ''')
    L = [list(map(int, line.split())) for line in sys.stdin]

    ans = chiness(L)
    if ans is None:
        print('\nРешений нет')
    else:
        x, M = ans
        print('\nx = {} + {}k, k = [1,2,3...]'.format(x, M))
