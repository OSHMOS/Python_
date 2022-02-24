# 1
A = int(input())
B = int(input())
print(A+B)

# 2
T = int(input())
A = 0
B = 0
for i in range(T):
    A, B = map(int, input().split())
    print(A+B)