class User:
    # 클래스 변수
    count = 0

    def __init__(self, name, email, pw):
        # 유저 인스턴스의 모든 변수를 지정해주는 메소드
        self.name = name
        self.email = email
        self.pw = pw

        User.count += 1

user1 = User("강영훈", "younghoon@codeit.kr", "123456")
user2 = User("이윤수", "yoonsoo@codeit.kr", "abcdef")
user3 = User("서혜린", "lisa@codeit.kr", "123abc")

User.count = 5

print(User.count)
print(user1.count)
print(user2.count)
print(user3.count)