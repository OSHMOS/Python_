N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
result = A + B
result = sorted(result)
print(*result)
