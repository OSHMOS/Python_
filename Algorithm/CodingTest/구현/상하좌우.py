import time

N = int(input())
list = list(input().split())
posX, posY = 1, 1

start_time = time.time()

for i in list:
    if i == 'L':
        posY -= 1
    elif i == 'R':
        posY += 1
    elif i == 'U':
        posX -= 1
    else:
        posX += 1

    if posX <= 0:
        posX += 1
    elif posY <= 0:
        posY += 1

print(posX, posY)

end_time = time.time()
print(f"time : {end_time - start_time}")