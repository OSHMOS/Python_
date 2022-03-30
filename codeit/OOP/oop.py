# 데코레이터 : 어떤 함수를 파라미터로 받아서 꾸며준 다음에 리턴해준다.
def add_print_to(original):
    def wrapper():
        print('함수 시작')
        original()
        print('함수 끝')
    return wrapper

@add_print_to
def print_hello():
    print('안녕하세요!')


print_hello()