# 메모리 : 34092 KB 시간 : 60 ms
from sys import stdin
from collections import Counter
t = int(input())
for _ in range(t):
    n = int(input())
    l = []
    for _ in range(n):
        ipt = list(stdin.readline().rstrip().split())
        l.append(ipt[-1])
    num = list(Counter(l).values())
    mul = 1
    if len(num) == 1:
        print(num[0])
    else:
        for i in num:
            mul *= i + 1
        print(mul - 1)
