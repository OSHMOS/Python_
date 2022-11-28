A, B = map(int, input().split())
result = 0
for i in str(A):
    for j in str(B):
        result += int(i) * int(j)
print(result)
