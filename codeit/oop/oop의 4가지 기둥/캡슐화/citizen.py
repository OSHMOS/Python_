'''
property 데코레이터 함수를 사용할 때
처음 코드를 짤 때, 캡슐화를 고려하지 않다가
추후에 캡슐화를 적용하고 싶을 때,
캡슐화를 적용하고 싶은 변수 이름으로 함수를 만들고
property 데코레이터를 그 함수 위에 표현해주면,
getter 함수로 사용 가능하고, 마찬가지로 setter 함수도 만들 수 있다.
'''
class Citizen:
    '''주민 클래스'''
    drinking_age = 19 # 음주 가능 나이

    def __init__(self, name, age, resident_id):
        '''이름, 나이, 주민등록번호'''
        self.name = name
        self.age = age
        self.resident_id = resident_id

    def authenticate(self, id_field):
        '''본인이 맞는지 확인하는 메소드'''
        return self.resident_id == id_field

    def can_drink(self):
        '''음주 가능 나이인지 확인하는 메소드'''
        return self.age >= Citizen.drinking_age

    # 원래 변수 이름이 붙여진 getter 함수를 만들면 된다.
    @property
    def age(self):
        print('나이를 리턴합니다.')
        return self._age

    # 이거는 setter 함수이다.
    @age.setter
    def age(self, value):
        print('나이를 설정합니다.')
        if value < 0:
            print('나이는 0보다 작을 수 없습니다. 기본 값 0으로 나이를 설정하겠습니다.')
            self._age = 0
        else:
            self._age = value

    def __str__(self):
        '''주민 정보를 문자열로 리턴하는 메소드'''
        return f'{self.name}씨는 {str(self.age)}살 입니다!'


osh = Citizen('oshmos', 26, '12345678')
print(osh.age)
osh.age = 30
print(osh.age)

