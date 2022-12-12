from itertools import combinations
N, M = map(int, input().split())
num_list = list(map(int, input().split()))
comb_list = list(combinations(num_list, 3))
temp_list = []
result = []
for comb in comb_list:
    temp_list.append(sum(comb))
for temp in temp_list:
    if temp <= M:
        result.append(temp)
print(max(result))
