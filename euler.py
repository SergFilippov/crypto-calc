import click
from factor import factorize, canonicalize


def euler(n):
    if n == 1:
        return 1

    res = 1
    for m, n in canonicalize(factorize(n)):
        res *= m ** n - m ** (n - 1)
    return res


if __name__ == '__main__':
    @click.command()
    @click.argument('a', type=click.INT)
    def cli(a):
        '''
        Расчет функции Эйлера

        A: целое число
        '''

        print("Euler(", a, ") = ", euler(a))
    cli()
