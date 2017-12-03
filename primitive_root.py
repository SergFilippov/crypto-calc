import click
from euler import euler
from factor import factorize


def primitive_root(m):
    c = euler(m)
    for a in range(2, c):
        if all((a ** (c // p)) % m != 1 for p in factorize(c)):
            return a


def reduced_residue_system(m):
    a = primitive_root(m)
    return [a ** i % m for i in range(euler(m))]


if __name__ == '__main__':
    @click.command()
    @click.argument('m', type=click.INT)
    def cli(m):
        '''
        Нахождение первообразного корня (образующего элемента) и формирование с его помощью приведенной системы вычетов

        M: модуль

        '''
        print("Первообразный корень: \t\t", primitive_root(m))
        print("Приведенная система вычетов: \t", reduced_residue_system(m))
    cli()
