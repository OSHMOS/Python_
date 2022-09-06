voca = input()
N = len(voca)
voca_10 = ''
cnt = 0
result = []
for i in range(N):
    voca_10 += voca[i]
    cnt += 1
    if cnt == 10:
        result.append(voca_10)
        voca_10 = ''
        cnt = 0
for i in result:
    print(i)
print(voca_10)  # 남은 것은 그냥 따로 출력해버리자. 된다.
