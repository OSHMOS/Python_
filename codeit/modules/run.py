# 권장하는 방법
from area import circle, square as sq

# 같은 이름의 함수는 마지막에 선언한 것이 정의된다.
# 같은 네임스페이스로 하지 않는 것이 좋다.
def square(length):
    return 4 * length

# 파일의 네임스페이스를 리턴
print(dir())
print(square(3))
print(sq(3))

