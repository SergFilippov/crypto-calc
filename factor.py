import click


def factorize(n):
    if n == 1:
        res = [1]
    else:
        res = []
        d = 2
        while d ** 2 <= n:
            if n % d == 0:
                res.append(d)
                n = n // d
            else:
                d += 1
        if n > 1:
            res.append(n)

    return res


def canonicalize(arr):
    res = {}
    for a in arr:
        if a in res:
            res[a] += 1
        else:
            res[a] = 1

    return sorted(res.items(), key=lambda t: t[0])


if __name__ == '__main__':
    @click.command()
    @click.argument('a', type=click.INT)
    def cli(a):
        '''
        Каноническое разложение на простые множители.

        A: целое число
        '''
        ans = ''
        for m, n in canonicalize(factorize(a)):
            if n == 1:
                ans += "{} * ".format(m)
            else:
                ans += "{}^{} * ".format(m, n)
        ans = ans[:-2]

        print(a, " = ", ans)
    cli()
