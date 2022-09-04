N, k = map(int, input().split())
grade_list = sorted(list(map(int, input().split())), reverse=True)
result = []
for i in range(k):
    result.append(grade_list[i])
print(min(result))
