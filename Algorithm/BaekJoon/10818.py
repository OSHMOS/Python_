num = int(input())
arr_num = list(map(int, input().split()))
arr = []

for i in range(num):
    arr.append(arr_num[i])

print(min(arr), max(arr))