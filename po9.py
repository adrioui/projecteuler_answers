from funcs import pita
from functools import reduce

print(max([(reduce(lambda m, n: m * n, pita(m, n))) for m in range(1, 21)
           for n in range(1, m) if reduce(lambda m, n: m + n, pita(m, n)) == 1000]))
