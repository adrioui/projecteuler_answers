from funcs import isPrime, computeFactors

print(
    [y for y in computeFactors(600851475143) if isPrime(y) == True][-1])
