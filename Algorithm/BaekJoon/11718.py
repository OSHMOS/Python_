# 입력값이 몇 번 주어지는지는 모르지만 -> 무한 반복
# 입력된 값 그대로 출력해야한다.
# EOFError -> 읽어들일 값이 없을 때 발생하는 에러

while True:
    try:
        print(input())
    except EOFError:
        break
