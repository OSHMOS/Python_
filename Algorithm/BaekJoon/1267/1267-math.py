# import 문제가 아니라면 뭔가 반례가 있나본데.. 잘 모르겠다.
import math
Y = 0
M = 0
N = int(input())
input_list = list(map(int, input().split()))
for i in range(N):
    cnt1 = math.ceil(input_list[i] / 30)
    cnt2 = math.ceil(input_list[i] / 60)
    Y += cnt1 * 10
    M += cnt2 * 15
if Y > M:
    print(f'M {M}')
elif Y < M:
    print(f'Y {Y}')
else:
    print(f'Y M {M}')
