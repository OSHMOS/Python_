n = int(input())
ar = []

for _ in range(n):
    ar.append(list(map(int, input().rstrip().split())))


def diagonalDifference(ar):
    sum1 = 0
    sum2 = 0
    for x in range(n):
        sum1 = sum1 + ar[x][x]
        sum2 = sum2 + ar[x][n - 1 - x]
    sub = sum1 - sum2
    result = abs(sub)
    return result


result = diagonalDifference(ar)
print(result)

# 1.   4번에서는 왜 from random import *를 안 써도 실행되는데 5번에서는 굳이 써야 실행되는 이유?
# -> 앞으로 randint 사용 시 오류 발생하면 바로 코드 맨 위에 from random import * 작성하기!

# 2.   i와 j를 쓰면 안되는 이유(추측) :
# -> 한 리스트 안에 3개의 다른 리스트가 저장되므로 행과 열로 생각할 수 없기 때문?
