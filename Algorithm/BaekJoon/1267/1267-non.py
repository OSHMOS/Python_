# 백준에서 import를 하면 안되나 보다.
Y = 0
M = 0
N = int(input())
input_list = list(map(int, input().split()))
for i in input_list:
    Y += i // 30 * 10 + 10
    M += i // 60 * 15 + 15
if Y > M:
    print(f'M {M}')
elif Y < M:
    print(f'Y {Y}')
else:
    print(f'Y M {M}')
