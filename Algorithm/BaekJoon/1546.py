sub_num = int(input())
score = list(map(int, input().split()))
max_score = max(score)
sum = 0

for i in range(sub_num):
    score[i] = score[i] / max_score * 100
    sum += score[i]
    new_ave = sum / sub_num

print(new_ave)