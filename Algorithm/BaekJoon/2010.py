import sys

N = int(input())
num_list = [int(sys.stdin.readline()) for _ in range(N)]
print(sum(num_list) - len(num_list) + 1)
