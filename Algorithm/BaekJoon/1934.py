# 메모리 : 32540 KB 시간 : 124 ms
import math
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(math.lcm(a, b))
