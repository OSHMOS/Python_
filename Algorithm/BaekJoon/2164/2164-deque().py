from collections import deque
N = int(input())
d = deque(i + 1 for i in range(N))
while True:
    if len(d) == 1:
        break
    d.popleft()
    d.append(d.popleft())

print(d[0])
