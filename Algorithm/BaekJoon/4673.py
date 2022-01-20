def d(n):
    num = list(str(n))
    for i in range(len(num)):
        n += int(num[i])
    return n

num_i = 1
while num_i <= 10000:
    if 1 <= d(num_i) <= 10000:
        continue
    else:
        print(num_i)

# 논리는 대충 이러하다.

