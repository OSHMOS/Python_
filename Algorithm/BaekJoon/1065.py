number = int(input())

cnt = 0
x = 1
while x <= number:
    for i in range(len(number) - 1):
        if number[i+1] - number[i] == number[i-1] - number[i+1]:
            cnt += 1

print(cnt)

# 1차 풀이