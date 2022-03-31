mutable_object = [1, 2, 3]
immutable_object = (1, 2, 3)

mutable_object[0] = 4
print(mutable_object)

# 불변 타입의 객체 요소는 바꿀 수 없다.
# immutable_object[0] = 4
# 불변 타입의 객체 자체의 인스턴스는 바꿀 수 있다.
immutable_object = (4, 1)
print(immutable_object)

# 가변 타입 : list, dict, 직접 작성하는 클래스
# 가변 타입은 새 인스턴스를 만들 필요 없이 원래 인스턴스의 속성을 바꾸면 된다.
# 불변 타입 : bool, int, float, str, tuple