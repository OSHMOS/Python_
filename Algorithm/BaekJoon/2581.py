# 소수 판별 문제에서 항상 염두에 두어야하는 점은 1은 소수가 아니라는 점이다.
import math

M = int(input())
N = int(input())
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

if result:
    print(sum(result))
    print(min(result))
else:
    print(-1)
