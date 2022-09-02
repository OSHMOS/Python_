input_list = list(map(int, input().split()))
base_list = [1, 1, 2, 2, 2, 8]
result_list = []
for i in range(6):
    result_list.append(base_list[i] - input_list[i])
print(*result_list)
