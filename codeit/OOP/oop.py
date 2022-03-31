class User:
    count = 0

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def say_hello(self):
        print(f"안녕하세요! 저는 {self.name}입니다.")

user1 = User('Young', 'young@codeit.kr', '123456')

print(type(user1))

# 파이썬은 순수 객체 지향 언어이다.
print(type(2))
print(type('string'))
print(type([]))
print(type({}))
print(type(()))

def print_hello():
    print('안녕하세요!')

print(type(print_hello))

int_list = []
int_list.append(1)
int_list.append(3)
int_list.append(7)

print(int_list)