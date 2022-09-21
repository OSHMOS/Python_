import sys
N = int(sys.stdin.readline())
result = []
for _ in range(N):
    cmd = sys.stdin.readline().split()
    if cmd[0] == 'push':
        result.append(cmd[1])
        # 정수 x를 스택에 넣는다.
    elif cmd[0] == 'pop':
        if len(result) == 0:
            print(-1)
        else:
            t = result.pop()
            print(t)
        # 스택에 있는 정수 하나를 빼고 그 수를 출력한다.
        # 스택에 정수가 없다면 -1을 출력한다.
    elif cmd[0] == 'size':
        print(len(result))
        # 스택에 들어있는 정수의 개수를 출력한다.
    elif cmd[0] == 'empty':
        if len(result) == 0:
            print(1)
        else:
            print(0)
        # 스택이 비어있으면 1 아니면 0을 출력한다.
    elif cmd[0] == 'top':
        if len(result) == 0:
            print(-1)
        else:
            print(result[-1])
        # 스택의 가장 위에 있는 정수를 출력한다. 없으면 -1을 출력한다.
