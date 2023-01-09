from math import factorial
n = int(input())
fac = list(str(factorial(n))).reverse()
cnt = 0
for i in fac:
    if i != '0':
        break
    cnt += 1
print(cnt)
