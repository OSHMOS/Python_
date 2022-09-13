import math

M, N = map(int, input().split())
result = []


def primeNumber(num):
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True


for i in range(M, N + 1):
    if i > 1:
        if primeNumber(i) == True:
            result.append(i)

for i in result:
    print(i)
