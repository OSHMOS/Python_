# 메모리 : 153964 KB 시간 : 1904 ms
from sys import stdin
N = int(stdin.readline())
arr = list(map(int, stdin.readline().rstrip().split()))
arr2 = list(sorted(set(arr)))

dic = {arr2[i]: i for i in range(len(arr2))}

for i in arr:
    print(dic[i], end=' ')
