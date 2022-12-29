import heapq
from sys import stdin
n = int(input())
heap = []
for _ in range(n):
    ipt = int(stdin.readline())
    if ipt != 0:
        heapq.heappush(heap, ipt)
    else:
        if len(heap) == 0:
            print(0)
            continue
        print(heapq.heappop(heap))
