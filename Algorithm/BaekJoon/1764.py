# set의 교집합 연산을 이용하는 것이 시간 줄이기에 더할 나위 없이 좋다.
N, M = map(int, input().split())
arr_1 = set()
arr_2 = set()
for _ in range(N):
    arr_1.add(input())
for _ in range(M):
    arr_2.add(input())
arr = sorted(list(arr_1 & arr_2))
print(len(arr))
for i in arr:
    print(i)
