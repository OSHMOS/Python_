num1, num2 = map(int, input().split())

list1 = list(str(num1))
list2 = list(str(num2))

list1.reverse()
list2.reverse()

result_num1 = ''
result_num2 = ''

for i in list1:
    result_num1 += i
for i in list2:
    result_num2 += i

result1 = int(result_num1)
result2 = int(result_num2)

if result2 > result1:
    print(result2)
elif result1 > result2:
    print(result1)