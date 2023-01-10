# 재귀함수와 메모이제이션
# 재귀함수는 시간 초과
'''
메모이제이션은 중간값이 한 번 뿐이라서,
한 번 더 같은 숫자를 넣으면 같은 값 출력 불가
'''
from sys import stdin
from functools import lru_cache

input = stdin.readline


@lru_cache(maxsize=None)
def fibonacci(n: int):
    global cnt0
    global cnt1
    if n == 0:
        cnt0 += 1
    elif n == 1:
        cnt1 += 1
    else:
        fibonacci(n - 1)
        fibonacci(n - 2)
        return 2


t = int(input())
for _ in range(t):
    cnt0 = 0
    cnt1 = 0
    n = int(input())
    fibonacci(n)
    print(cnt0, cnt1)
