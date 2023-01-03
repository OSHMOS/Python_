result = []
for _ in range(7):
    num = int(input())
    if num % 2 == 1:
        result.append(num)
if len(result) != 0:
    print(sum(result))
    print(min(result))
else:
    print(-1)
