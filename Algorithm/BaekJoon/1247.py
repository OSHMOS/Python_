from sys import stdin

result = []
for _ in range(3):
    num = [int(stdin.readline()) for _ in range(int(stdin.readline()))]
    if sum(num) == 0:
        result.append('0')
    elif sum(num) > 0:
        result.append('+')
    else:
        result.append('-')
for i in result:
    print(i)
