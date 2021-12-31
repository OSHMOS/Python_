test_num = int(input())

for i in range(test_num):
    test_case = list(input())
    sum_cnt = 0
    cnt = 0
    for k in test_case:
        if k == 'O':
            cnt += 1
            sum_cnt += cnt
        else:
            cnt = 0
    print(sum_cnt)