from random import *

n = int(input())
ar = []

for i in range(1, n):
    a = randint(-2147483648, 2147283647)
    ar.append(a)


def aVeryBigSum(ar):
    x = 0
    for i in range(0, n - 1):
        x = x + ar[i]
    return x


result = aVeryBigSum(ar)
print(result)