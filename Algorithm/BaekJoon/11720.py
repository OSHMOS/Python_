# 첫 번째 방법
n = input()
print(sum(map(int, input())))

# 두 번째 방법
test_num = int(input())
nums = input()
total = 0
for i in nums:
    total += int(i)
print(total)

# 세 번째 방법
for i in range(test_num):
    total += int(nums[i])
print(total)


