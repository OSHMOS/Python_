# 클래스
# 인스턴스 메소드의 첫 번째 파라미터는 꼭 self로 쓰는 것을 권장함
class User:
    # magic method (special method) 특수 메소드
    # 인스턴스가 생성될 때 자동으로 호출
    # 클래스 작성 시 꼭 작성할 것!
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        
    def say_hello(self):
        # 인사 메세지 출력 메소드
        print(f"안녕하세요! 저는 {self.name}입니다!")

    def login(self, my_email, my_password):
        if self.email == my_email and self.password == my_password:
            print("로그인 성공, 환영합니다.")
        else:
            print("로그인 실패, 없는 아이디이거나 잘못된 비밀번호입니다.")

    def check_name(self, name):
        # 파라미터로 받는 name이 유저의 이름과 같은지 불 값으로 리턴하는 메소드
        return self.name == name

# 객체 (인스턴스)
user1 = User("Young", "young@codeit.kr", "123456")

user2 = User("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")

user3 = User("Taeho", "taeho@codeit.kr", "123abc")

user4 = User("Lisa", "list@codeit.kr", "abc123")

# 출력하기
print(user1.email)
print(user2.name)
print(user3.password)
print(user4.email)