class User:
    count = 0

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

        User.count += 1

    def say_hello(self):
        print(f"안녕하세요! 저는 {self.name}입니다.")

    def __str__(self):
        return f"사용자 : {self.name}, 이메일 : {self.email}, 비밀번호 : ******"

    # 클래스 메소드 (인스턴스 변수를 사용하지 않기 때문)
    @classmethod
    def number_of_users(cls):
        print(f"총 유저 수는 : {cls.count}")

# 첫 번째 파라미터로 클래스가 자동 전달
User.number_of_users()