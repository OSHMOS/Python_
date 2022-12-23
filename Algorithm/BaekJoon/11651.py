from sys import stdin
N = int(stdin.readline())
result = []
for _ in range(N):
    [x, y] = map(int, stdin.readline().split())
    result.append([y, x])
for i in sorted(result):
    i.reverse()
    print(*i)
