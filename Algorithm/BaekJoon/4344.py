test_num = int(input())
score = list(map(int, input().split())) # 총 6개
bigger_ave = 0
for i in range(1, len(score)):
    ave = sum(score) / score[0]
    if score[i] > ave:
        bigger_ave += 1

result = bigger_ave / score[0] * 100
print(f"{result:0.3f}%")