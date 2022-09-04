T = int(input())
result_list = []
for i in range(T):
    score_list = sorted(list(map(int, input().split())), reverse=True)
    score_list.pop(0)
    score_list.pop(-1)
    if score_list[0] - score_list[-1] >= 4:
        result_list.append('KIN')
    else:
        result_list.append(sum(score_list))
for i in result_list:
    print(i)
