# 메모리 : 46752 KB | 시간 : 4200 ms
N = int(stdin.readline())
result = []
for _ in range(N):
    [x, y] = map(int, input().split())
    result.append([x, y])
for i in sorted(result):
    print(*i)
