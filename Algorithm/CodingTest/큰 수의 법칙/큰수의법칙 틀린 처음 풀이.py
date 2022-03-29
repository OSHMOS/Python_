# 앞으로 주석 쓰는 법을 다시 들여야겠다.
# 코드 내용이 아무것도 기억이 안난다.
import time

N, M, K = map(int, input().split())
result = 0
cnt = 0


for i in range(N):
    num = input()
    list.append(num)
temp = sorted(list, reverse=True)

start_time = time.time()
for i in range(M):
    if cnt == K-1:
        result += int(temp[1])
        cnt = 0
    else:
        result += int(temp[0])
        cnt += 1
print(result)

end_time = time.time()
print(f"time : {end_time - start_time}")
