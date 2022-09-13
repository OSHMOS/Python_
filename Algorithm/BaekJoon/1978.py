# 소수 판별 원리는 이해하였음
import math

N = int(input())
input_list = list(map(int, input().split()))
cnt = 0


def primeNumber(num):
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True


for i in input_list:
    if i > 1:
        if primeNumber(i) == True:
            cnt += 1

print(cnt)
