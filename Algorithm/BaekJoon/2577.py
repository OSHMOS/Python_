num1 = int(input())
num2 = int(input())
num3 = int(input())
arr = []

multiple_result = num1 * num2 * num3
multiple_result_array = str(multiple_result)

for i in range(10):
    arr.append(0)
    for j in multiple_result_array:
        if int(j) == i:
            arr[i] += 1
    print(arr[i])




