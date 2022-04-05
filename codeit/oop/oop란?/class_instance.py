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

    # double underscore : dunder
    def __str__(self):
        return f"사용자 : {self.name}, 이메일 : {self.email}, 비밀번호 : ******"

# 객체 (인스턴스)
user1 = User("Young", "young@codeit.kr", "123456")
user2 = User("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")

# 출력하기
print(user1)
print(user2)