import click
from primitive_root import reduced_residue_system
from congruences import congruence


def exponential_congruence(a, b, m):
    a %= m
    b %= m
    index = lambda x, m: reduced_residue_system(m).index(x)
    return congruence(index(a, m), index(b, m), m - 1)


if __name__ == '__main__':
    @click.command()
    @click.argument('a', type=click.INT)
    @click.argument('b', type=click.INT)
    @click.argument('m', type=click.INT)
    def cli(a, b, m):
        '''
        Решение сравнения A ^ x ≡ B (mod M)

        A, B, M: целые числа
        '''

        print("{} ^ x ≡ {}(mod {})".format(a, b, m))
        ans = exponential_congruence(a, b, m)

        if ans is None:
            print('Решений нет')
        else:
            print("x =", ans[0], "+", ans[1], "* k, k = [1, 2, 3...]")
    cli()
