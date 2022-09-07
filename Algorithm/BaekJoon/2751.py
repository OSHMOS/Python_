# 입력받는 수가 더 커져서 stdin으로 받아야 합니다.
from sys import stdin
N = int(input())
input_list = []
for i in range(N):
    num = int(stdin.readline())
    input_list.append(num)
for i in sorted(input_list):
    print(i)
