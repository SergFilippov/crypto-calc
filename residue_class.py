import click
from factor import factorize, canonicalize
from chiness import chiness
import math


def residue_class(a, k, m):
    if is_prime(m):
        p = m - 1
        k = k % p
        x = a ** k % m
        return x, m

    else:
        p_arr, n_arr = list(map(list, zip(*canonicalize(factorize(m)))))
        if any(n > 1 for n in n_arr):
            return None

        system = [[a ** (k % (p - 1)) % p, p] for p in p_arr]
        return chiness(system)


def is_prime(n):
    for i in range(2, int(math.ceil(math.sqrt(n)))):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    @click.command()
    @click.argument('a', type=click.INT)
    @click.argument('k', type=click.INT)
    @click.argument('m', type=click.INT)
    def cli(a, k, m):
        '''
        Нахождение вычета a^k(mod m)

        '''
        print("{} ^ {} ≡ x (mod {})".format(a, k, m))
        ans = residue_class(a, k, m)
        if ans is None:
            print('\nРешений нет')
        else:
            x, M = ans
            print('\nx = {} + {}k, k = [1,2,3...]'.format(x, M))
    cli()
