arr = []

for i in range(9):
    num = int(input())
    arr.append(num)

    if arr[i] == max(arr):
        nth_num = i + 1  # index와 몇 번째는 1의 차이가 난다.

print(max(arr))
print(nth_num)

