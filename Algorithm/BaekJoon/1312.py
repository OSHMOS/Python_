A, B, N = map(int, input().split())
for i in range(1, N):
    A = (A % B) * 10
    result = A // B
print(result)
