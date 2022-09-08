input_list = list(map(int, input().split()))
sum_2 = 0
for i in input_list:
    sum_2 += i ** 2
print(sum_2 % 10)
