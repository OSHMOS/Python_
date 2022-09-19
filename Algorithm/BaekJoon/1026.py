N = int(input())
A = sorted(list(map(int, input().split())), reverse=True)
B = sorted(list(map(int, input().split())))
s = 0
for i in range(N):
    s += A[i] * B[i]
print(s)
