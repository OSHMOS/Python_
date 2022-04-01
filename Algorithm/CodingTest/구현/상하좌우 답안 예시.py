import time

# N을 입력 받기
n = int(input())
x, y = 1, 1
plans = input().split()

start_time = time.time()
# L, R, U, D에 따른 이동 방향
# 이 구현이 진짜 대단하다고 생각됨
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
  # 이동 후 좌표 구하라
  for i in range(len(move_types)):
    if plan == move_types[i]:
      nx = x + dx[i]
      ny = y + dy[i]
  # 공간을 벗어나는 경우 무시
  if nx < 1 or ny < 1 or nx > n or ny > n:
    continue
  # 이동 수정
  x, y = nx, ny

print(x, y)

end_time = time.time()
print(f"time : {end_time - start_time}")