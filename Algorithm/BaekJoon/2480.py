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

print(len(list_num))

# 분명히 두 번째 조건을 좀 더 쉽게 쓸 수 있을 것 같은데