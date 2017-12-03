import click
from euclid import euclid


def inverse_element(a, m):
    nod, u, v = euclid(a, m)
    if nod != 1:
        return None
    elif u < 0:
        return m + u
    return u


if __name__ == '__main__':
    @click.command()
    @click.argument('a', type=click.INT)
    @click.argument('m', type=click.INT)
    def cli(a, m):
        '''
        Обратный элемент по модулю

        A: элемент
        M: модуль
        '''
        ans = inverse_element(a, m)
        if ans is None:
            print('Обратного элемента не существует')
        else:
            print(ans)
    cli()
