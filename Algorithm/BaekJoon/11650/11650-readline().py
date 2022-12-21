# 메모리 : 46752 KB | 시간 : 364 ms
from sys import stdin
N = int(stdin.readline())
result = []
for _ in range(N):
    [x, y] = map(int, stdin.readline().split())
    result.append([x, y])
for i in sorted(result):
    print(*i)
