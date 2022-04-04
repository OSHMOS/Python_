class User:
    count = 0
    
    def __init__(self, name, email, pw):
        self.name = name
        self.email = email
        self.pw = pw
    
        User.count += 1
    
    def say_hello(self):
        print("안녕하세요! 저는 {}입니다!".format(self.name))
    
    def __str__(self):
        return "사용자: {}, 이메일: {}, 비밀번호: ******".format(self.name, self.email)
    
    @classmethod
    def number_of_users(cls):
        print("총 유저 수는: {}입니다".format(cls.count))
    
    # 자동 전달되는 파라미터가 없는 정적 메소드
    # 인스턴스 변수나 클래스 변수 중 아무것도 사용하지 않을 메소드
    @staticmethod
    def is_valid_email(email_address):
        return "@" in email_address

user1 = User("강영훈", "younghoon@codeit.kr", "123456")

print(User.is_valid_email("taehosung"))
print(User.is_valid_email("taehosung@codeit.kr"))
    
print(user1.is_valid_email("taehosung"))
print(user1.is_valid_email("taehosung@codeit.kr"))