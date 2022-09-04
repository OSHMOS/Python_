w_score = []
k_score = []
w_sum = 0
k_sum = 0
for i in range(20):
    score = int(input())
    if i >= 0 and i <= 9:
        w_score.append(score)
    else:
        k_score.append(score)
for i in range(3):
    w_sum += sorted(w_score, reverse=True)[i]
    k_sum += sorted(k_score, reverse=True)[i]
print(w_sum, k_sum)
