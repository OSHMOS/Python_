list_num = list(map(int, input().split()))

if list_num[0] == list_num[1] == list_num[2]:
    print(10000 + max(list_num) * 1000)
elif list_num[0] == list_num[1]:
    print(1000 + list_num[0] * 100)
elif list_num[0] == list_num[2]:
    print(1000 + list_num[2] * 100)
elif list_num[1] == list_num[2]:
    print(1000 + list_num[1] * 100)
else:
    print(max(list_num) * 100)

# 분명히 두 번째 조건을 좀 더 쉽게 쓸 수 있을 것 같은데
# 무작정 차례대로 풀었는데 조금 멀리서 문제를 보는 습관을 들여야 할 것 같다.
# 첫 번째와 세 번째 조건이 간단해서 먼저 작성하고 마지막 조건이 여집합임을 알았다면
# 조금 더 쉽게 풀 수 있었다.

numbers = list(map(int, input().split()))
set_numbers = set(numbers)

if len(set_numbers) == 1:
    print(10000 + numbers[0] * 1000)

elif len(set_numbers) == 3:
    print(max(numbers) * 100)

else:
    numbers.sort()
    print(1000 + numbers[1] * 100)