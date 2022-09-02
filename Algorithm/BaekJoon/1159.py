# count는 리스트에서도 가능하다.
name_list = sorted([input()[0] for _ in range(int(input()))])
name_set = set(name_list)
res = []
for name in name_set:
    if name_list.count(name) >= 5:
        res.append(name)
print(''.join(sorted(res) if len(res) > 0 else 'PREDAJA'))
