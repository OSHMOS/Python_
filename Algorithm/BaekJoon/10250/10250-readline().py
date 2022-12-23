from sys import stdin
T = int(stdin.readline())
for _ in range(T):
    room = []
    H, W, N = map(int, stdin.readline().split())
    for j in range(1, W + 1):
        for i in range(1, H + 1):
            if j < 10:
                room.append(f'{i}0{j}')
            else:
                room.append(f'{i}{j}')
    print(room[N - 1])
