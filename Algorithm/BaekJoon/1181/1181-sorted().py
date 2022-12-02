# sorted()는 틀리고,
N = int(input())
voca_list = sorted([input() for _ in range(N)])
print(voca_list)
voca_set = set(voca_list)
voca_list = list(voca_set)
voca_list.sort(key=len)
for voca in voca_list:
    print(voca)
