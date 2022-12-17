import sys
from collections import Counter
N = int(sys.stdin.readline())
base_list = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
base_list_count = {}
result_list = [0 for _ in range(M)]
for i in set(base_list):
    base_list_count[i] = base_list.count(i)
for i in range(M):
    if num_list[i] in base_list_count:
        result_list[i] += base_list_count[num_list[i]]
    else:
        continue
print(*result_list)
