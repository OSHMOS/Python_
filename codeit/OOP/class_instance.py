# 클래스
class User:
    def say_hello(some_user):
        # 인사 메세지 출력 메소드
        print(f"안녕하세요! 저는 {some_user.name}입니다!")

    def login(some_user, my_email, my_password):
        if some_user.email == my_email and some_user.password == my_password:
            print("로그인 성공, 환영합니다.")
        else:
            print("로그인 실패, 없는 아이디이거나 잘못된 비밀번호입니다.")

# 객체 (인스턴스)
user1 = User()
user2 = User()
user3 = User()

# 인스턴스 변수 (속성) 추가하기
user1.name = "김대위"
user1.email = "captain@codeit.kr"
user1.password = "12345"

# 출력하기
User.say_hello(user1)
user1.say_hello() # 파라미터를 따로 써 줄 필요가 없는 형태
user1.login("captain@codeit.kr", "12345")