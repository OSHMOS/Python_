cnt = 0
result = []
for _ in range(4):
    A, B = map(int, input().split())
    cnt -= A
    cnt += B
    result.append(cnt)
print(max(result))
