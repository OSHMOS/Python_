result = []
for _ in range(5):
    grade = int(input())
    result.append(grade if grade >= 40 else 40)
print(sum(result) // 5)
