from sys import stdin
from collections import deque
t = int(input())
for _ in range(t):
    ipt = stdin.readline().rstrip()
    num = int(input())
    flag = 1
    arr = stdin.readline().rstrip()
    dq = deque(list(arr[1:-1].split(',')))
    if num == 0:
        dq = deque()
    R = 0
    for i in ipt:
        if i == 'R':
            R += 1
        elif i == 'D':
            if len(dq) == 0:
                print('error')
                flag = 0
                break
            else:
                if R % 2 == 0:
                    dq.popleft()
                else:
                    dq.pop()
    if flag == 0:
        continue
    else:
        if R % 2 == 0:
            print('[' + ','.join(dq) + ']')
        else:
            dq.reverse()
            print('[' + ','.join(dq) + ']')
