import click
from functools import reduce
from factor import factorize
from residue_class import is_prime

def legendre_symbol(a, p):
    if not is_prime(p):
        return None
    if a == 0:
        return 0
    elif a == 1:
        return 1
    elif a % 2 == 0:
        return legendre_symbol(a // 2, p) * ((-1) ** (((p ** 2) - 1) // 8))
    else:
        return legendre_symbol(p % a, a) * ((-1) ** ((a - 1) * (p - 1) // 4))

def jacobi_symbol(a, n):
    return reduce(lambda x, y: x * legendre_symbol(a, y), factorize(n), 1)

if __name__ == '__main__':
    @click.command()
    @click.argument('a', type=click.INT)
    @click.argument('n', type=click.INT)
    def cli(a, n):
        '''
        Нахождение символа Лежандра и символа Якоби

        A, N: целые числа

        '''
        print("Символ Лежандра: \t",legendre_symbol(a, n))
        print("Символ Якоби: \t\t", jacobi_symbol(a, n))
    cli()
