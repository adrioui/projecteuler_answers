from funcs import computeFibo


total = 0
i = 1
while computeFibo(i) <= 4000000:
    if computeFibo(i) % 2 == 0:
        total += computeFibo(i)
    i += 1
print(total)
