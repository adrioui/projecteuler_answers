from functools import reduce

num = reduce(lambda x, y: x * y, range(1, 101))

num = str(num)

num = [int(n) for n in num]

print(reduce(lambda x, y: x + y, num))
