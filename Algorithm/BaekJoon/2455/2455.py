pass_cnt = 0
result = []
for _ in range(4):
    pass_list = list(map(int, input().split()))
    pass_cnt -= pass_list[0]
    pass_cnt += pass_list[1]
    result.append(pass_cnt)
print(max(result))
