from sys import stdin
N = int(stdin.readline())
for _ in range(N):
    is_it_vps = stdin.readline().rstrip()
    stack = []
    stop = 0
    for i in is_it_vps:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack:  # 스택에 요소 있으면 pop()
                stack.pop()
            else:      # 스택이 비었으면 stop 올리고 break
                stop += 1
                break
    if stack or stop > 0:  # 스택이 안비었거나 stop이 양수면 NO
        print('NO')
    else:               # 스택이 비었으면 YES
        print('YES')
