test_num = int(input())
score = []
j = 0
for i in range(test_num):
    test_case = list(input())
    while j < len(test_case):
        if test_case[j] == 0:
            score[j] = 1
            if test_case[j + 1] == 0:
                score[j + 1] = 2


    print(test_case)

# 어떤 식으로 각 항을 비교하여 점수를 추가하는 것이 좋을지 생각 좀 해봐야겠다.