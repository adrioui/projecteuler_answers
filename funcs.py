from functools import lru_cache


@lru_cache(maxsize=1000)
def computeFibo(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return computeFibo(n - 1) + computeFibo(n - 2)


def isPrime(n):
    if n == 2:
        return True
    elif n < 2:
        return False
    elif n % 2 == 0:
        return False
    else:
        return all(
            [n % x for x in range(3, (1 + int(n ** 0.5)))])


def computeFactors(num):
    return [x for x in
            range(1, (1 + int(num ** 0.5))) if num % x == 0]


def sieveOfEratosthenes(limit):
    a = [True] * limit

    for (i, isPrime) in enumerate(a, start=2):
        if isPrime:
            yield i
            for j in range(i * i, limit, i):
                a[j] = False


def pita(m, n):
    if m > n:
        a = m ** 2 - n ** 2
        b = 2 * m * n
        c = m ** 2 + n ** 2
    elif m < n or m == n:
        return "m should be greater than n"

    return [a, b, c]
