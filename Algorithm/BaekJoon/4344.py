test_num = int(input())
score = list(map(int, input().split())) # 총 6개
# test_num을 받았으니까 이용해야 하는데 어떻게 이용해야 할 지 감이 잡히질 않는다.
bigger_ave = 0
for i in range(1, len(score)):
    ave = sum(score) / score[0]
    if score[i] > ave:
        bigger_ave += 1

result = bigger_ave / score[0] * 100
print(f"{result:0.3f}%")