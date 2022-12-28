N = int(input())
per_time_list = list(map(int, input().split()))
min_time_list = sorted(per_time_list)
temp = 0
min_sum = 0
for i in min_time_list:
    temp += i
    min_sum += temp
print(min_sum)
