from sys import stdin
n, m = map(int, stdin.readline().split())
ipt_list = list(map(int, stdin.readline().split()))
sum_value = 0
prefix_sum = [0]
for i in ipt_list:
    sum_value += i
    prefix_sum.append(sum_value)
for _ in range(m):
    i, j = map(int, stdin.readline().split())
    print(prefix_sum[j] - prefix_sum[i-1])
