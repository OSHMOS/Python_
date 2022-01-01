test_num = int(input())
for i in range(test_num):
    repeat_num, test_case = input().split()
    repeat_int = int(repeat_num)
    for k in test_case:
        print(k * repeat_int)

# 무엇이 문제인지 모르겠다. 한 줄씩 나오는 게 문제인가??
