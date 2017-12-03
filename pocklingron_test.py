from itertools import count, islice
import click
from factor import factorize
from euclid import euclid


def a_generator(p):
    for a in count(2):
        if (a ** (p - 1) % p == 1):
            yield a


def is_prime(p):
    q = max(factorize(p-1))
    if p > (q + 1) ** 2:
        return None
    for a in islice(a_generator(p), 3):
        if euclid(a ** ((p - 1) // q) - 1, p)[0] == 1:
            return True

    return None


if __name__ == '__main__':
    @click.command()
    @click.argument('n', type=click.INT)
    def cli(n):
        '''
        N: целое число

        Критерий Поклингтона — детерминированный тест на простоту

        '''
        if is_prime(n):
            print("{} - простое число".format(n))
        else:
            print("{} - возможно составное число".format(n))
    cli()
