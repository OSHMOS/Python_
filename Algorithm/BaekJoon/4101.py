# 마지막 줄 '0 0' 입력 시 아무것도 출력을 안하는 것을 보고 반복문 종료를 예측할 줄 알아야 함
# 자신을 믿자.
while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    elif A > B:
        print('Yes')
    else:
        print('No')
