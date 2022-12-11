N, M = map(int, input().split())

board_a = []
board_b = []
board_result = [[0 for _ in range(M)] for _ in range(N)]

for _ in range(N):
    board_a.append(list(map(int, input().split())))
for _ in range(N):
    board_b.append(list(map(int, input().split())))

for row in range(N):
    for col in range(M):
        print(board_a[row][col] + board_b[row][col], end=' ')
    print()  # 줄 마다 엔터키를 치는 용도다.
