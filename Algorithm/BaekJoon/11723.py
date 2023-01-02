from sys import stdin
m = int(stdin.readline())
s = set()
for _ in range(m):
    cmd = list(stdin.readline().rstrip().split())
    if cmd[0] == 'all' or cmd[0] == 'empty':
        num = 0
    else:
        num = int(cmd[-1])
    if cmd[0] == 'add':
        s.add(num)
    elif cmd[0] == 'remove':
        s.discard(num)
    elif cmd[0] == 'check':
        if num in s:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'toggle':
        if num in s:
            s.remove(num)
        else:
            s.add(num)
    elif cmd[0] == 'all':
        s = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
                 12, 13, 14, 15, 16, 17, 18, 19, 20])
    elif cmd[0] == 'empty':
        s.clear()
