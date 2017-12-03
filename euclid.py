import click


def euclid(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = euclid(b, a % b)
        return d, y, x - y * (a // b)


if __name__ == '__main__':
    @click.command()
    @click.argument('a', type=click.INT)
    @click.argument('b', type=click.INT)
    def cli(a, b):
        '''
        A, B: целые числа

        Расширенный алгоритм Евклида находит НОД(a, b), а также коэффициенты u и v такие, что:

        \ta * u + b * v = НОД(a, b).

        '''
        nod, u, v = euclid(a, b)
        print("НОД({}, {}) = ".format(a, b), nod)

        print('u = ', u)
        print('v = ', v)

    cli()
