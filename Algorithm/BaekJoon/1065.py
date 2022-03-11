num = int(input())
cnt = 0
for n in range(1, num+1):
    if n < 100:
        cnt += 1
    elif n >= 100 and n <= 1000:
        nums = list(map(int, str(num)))
        if nums[2] - nums[1] == nums[1] - nums[0]:
            cnt += 1

print(cnt)