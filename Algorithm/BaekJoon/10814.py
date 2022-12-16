import sys
N = int(sys.stdin.readline())
d = []
for _ in range(N):
    age, name = map(str, sys.stdin.readline().split())
    age = int(age)
    d.append([age, name])
d.sort(key=lambda x: x[0])
for i in d:
    print(i[0], i[1])
