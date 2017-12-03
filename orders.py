from euler import euler
import click

def get_divisors(a):
    return [i for i in range(1, a + 1) if a % i == 0]

def multy_orders(m):
    f = euler(m)
    divisors = get_divisors(f)
    orders = {}
    for i in range(2, f + 1):
        for divisor in divisors:
            if (i ** divisor) % m == 1:
                orders[i] = divisor
                break
    return orders

def additive_orders(m):
    divisors = get_divisors(m)
    orders = {}
    for i in range(0, m):
        if i == 1:
            continue
        for divisor in divisors:
            if (i * divisor) % m == 0:
                orders[i] = divisor
                break
    return orders


if __name__ == '__main__':
    @click.command()
    @click.argument('a', type=click.INT)
    def cli(a):
        '''
        Нахождение порядка всех элементов в группе
        A: целое число
        '''
        print('Аддитивная группа: ', additive_orders(a))
        print('Мультипликаивная группа: ', multy_orders(a))

    cli()
