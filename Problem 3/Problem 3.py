def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, round(n/2)):
        if n % i == 0:
            return False
    return True

x = 600851475143
factor = 2
lastFactor = 1

for i in range(1, x+1):
    if x % i == 0 and isPrime(x/i):
        print(round(x/i), "is prime.")
        break