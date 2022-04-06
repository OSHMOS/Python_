'''
클래스를 개발하는 개발자는 필요해보이는 모든 메소드를 만들어 놓고
클래스를 사용하는 개발자는 변수를 직접 가져다 쓰기 전에 사용할 메소드가 있는지 찾아보고
이렇게
변수를 직접 사용하는 것을 최소화해야
유지보수가 쉬운 코드를 만들 수 있다.
=> 객체를 사용할 땐 최대한 메소드로!
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

