import sys
from collections import deque
d = deque()
N = int(input())
for _ in range(N):
    do = list(sys.stdin.readline().split())
    if do[0] == 'push_front':
        d.appendleft(do[1])
    elif do[0] == 'push_back':
        d.append(do[1])
    elif do[0] == 'pop_front':
        if len(d) == 0:
            print(-1)
        else:
            print(d[0])
            d.popleft()
    elif do[0] == 'pop_back':
        if len(d) == 0:
            print(-1)
        else:
            print(d[-1])
            d.pop()
    elif do[0] == 'size':
        print(len(d))
    elif do[0] == 'empty':
        if len(d) == 0:
            print(1)
        else:
            print(0)
    elif do[0] == 'front':
        if len(d) == 0:
            print(-1)
        else:
            print(d[0])
    elif do[0] == 'back':
        if len(d) == 0:
            print(-1)
        else:
            print(d[-1])
