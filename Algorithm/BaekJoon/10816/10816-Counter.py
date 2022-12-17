import sys
from collections import Counter
N = int(sys.stdin.readline())
base_list = sys.stdin.readline().split()
M = int(sys.stdin.readline())
num_list = sys.stdin.readline().split()
base_list_count = Counter(base_list)
result_list = []
for i in num_list:
    if i in base_list_count:
        result_list.append(base_list_count[i])
    else:
        result_list.append(0)
print(*result_list)
