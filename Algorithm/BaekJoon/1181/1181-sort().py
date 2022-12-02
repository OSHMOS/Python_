# sort()는 왜 맞을까?
N = int(input())
voca_list = [input() for _ in range(N)]
voca_set = set(voca_list)
voca_list = list(voca_set)
voca_list.sort()
voca_list.sort(key=len)
for voca in voca_list:
    print(voca)
