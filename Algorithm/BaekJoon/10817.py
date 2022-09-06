input_list = sorted(list(map(int, input().split())))
input_list.pop(0)
input_list.pop(-1)
print(*input_list)
