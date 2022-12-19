# 시간 초과가 뜸
N = int(input())
l = [i+1 for i in range(N)]
while True:
    if len(l) == 1:
        break
    l.pop(0)
    l.append(l.pop(0))

print(*l)
