test_num = int(input())
for i in range(test_num):
    repeat_num, test_case = input().split()
    text = ''
    for k in test_case:
        text += k * int(repeat_num)
    print(text)

# 무엇이 문제인지 모르겠다. 한 줄씩 나오는 게 문제인가??
# 한 줄씩 나오는 게 문제였다.
