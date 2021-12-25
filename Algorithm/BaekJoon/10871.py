num, X = map(int, input().split())
arr = input().split()
Arr = []
for i in range(num):
    if int(arr[i]) < X:
        Arr.append(int(arr[i]))

for i in Arr:
    print(i)