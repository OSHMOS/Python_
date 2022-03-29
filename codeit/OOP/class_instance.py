# 클래스
class User:
    def say_hello(some_user):
        # 인사 메세지 출력 메소드
        print(f"안녕하세요! 저는 {some_user.name}입니다!")

# 객체 (인스턴스)
user1 = User()
user2 = User()
user3 = User()

# 인스턴스 변수 (속성) 추가하기
user1.name = "김대위"
user1.email = "captain@codeit.kr"
user1.password = "12345"

user2.name = "강영훈"
user2.email = "younghoon@codeit.kr"
user2.password = "98765"

user3.name = "최지웅"
user3.email = "jiwoong@codeit.kr"
user3.password = "78945"

# 출력하기
print(user1.email)
print(user2.password)
# 정의하지 않은 인스턴스 변수는 사용할 수 없다.
# 인스턴스 변수를 사용하려면 미리 정의해야 한다.
# print(user1.age)
User.say_hello(user1)
User.say_hello(user2)
User.say_hello(user3)