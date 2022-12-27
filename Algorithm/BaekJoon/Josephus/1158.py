from sys import stdin
from collections import deque
n, k = map(int, stdin.readlin().split())
s = deque([])
for i in range(1, n + 1):
    s.append(i)
print('<', end='')
while s:
    for _ in range(k - 1):
        s.append(s[0])
        s.popleft()
    print(s.popleft(), end='')
    if s:
        print(', ', end='')
print('>')
