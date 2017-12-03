import click
from euclid import euclid
from inverse_element import inverse_element


def congruence(a, b, m):
    nod, _, _ = euclid(a, m)
    if b % nod != 0:
        return None

    if nod != 1:
        a, b, m = map(lambda x: x//nod, (a, b, m))

    inv = inverse_element(a, m)
    if inv is None:
        return None
    else:
        return b * inv % m, m


if __name__ == '__main__':
    @click.command()
    @click.argument('a', type=click.INT)
    @click.argument('b', type=click.INT)
    @click.argument('m', type=click.INT)
    def cli(a, b, m):
        '''
        Решение сравнения A * x ≡ B (mod M)

        A, B, M: целые числа
        '''

        print("{} * x ≡ {}(mod {})".format(a, b, m))
        ans = congruence(a, b, m)

        if ans is None:
            print('Решений нет')
        else:
            print("x =", ans[0], "+", ans[1], "* k, k = [1, 2, 3...]")
    cli()
