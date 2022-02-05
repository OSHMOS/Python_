N, M, K = map(int, input().split())
list = []
result = 0
cnt = 0

for i in range(N):
    num = int(input())
    list.append(num)
temp = sorted(list, reverse=True)

for i in range(M):
    if cnt == K-1:
        result += temp[1]
        cnt = 0
    else:
        result += temp[0]
        cnt += 1
print(result)
