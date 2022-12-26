from sys import stdin
n, m = map(int, stdin.readline().split())
poketmon1 = {}
poketmon2 = {}
for i in range(1, n + 1):
    name = stdin.readline().rstrip()
    poketmon1[name] = i
    poketmon2[i] = name

for i in range(m):
    quiz = stdin.readline().rstrip()
    if quiz.isdigit():
        print(poketmon2[int(quiz)])
    else:
        print(poketmon1[quiz])
