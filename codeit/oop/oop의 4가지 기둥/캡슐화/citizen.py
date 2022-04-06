'''
캡슐화 정리
1. 클래스 밖에서 접근 못하게 할 변수, 메소드 정하기
2. 변수나 메소드 이름 앞에 언더바 2개 붙이기 => 1개만 붙여도 된다.
2-1. 1개만 붙이는 것은 사실 아무 기능이 없지만 (외부에서 접근 가능하지만)
     파이썬 개발자들만의 문화이기 때문에 꼭 경고를 지켜야한다.
3. 변수에 간접 접근할 수 있게 메소드 추가하기 (getter/setter) or 다른 용도의 메소드
'''
class Citizen:
    '''주민 클래스'''
    drinking_age = 19 # 음주 가능 나이

    def __init__(self, name, age, resident_id):
        '''이름, 나이, 주민등록번호'''
        self.name = name
        self._age = age
        self._resident_id = resident_id

    def authenticate(self, id_field):
        '''본인이 맞는지 확인하는 메소드'''
        return self._resident_id == id_field

    def can_drink(self):
        '''음주 가능 나이인지 확인하는 메소드'''
        return self._age >= Citizen.drinking_age

    def get_age(self):
        '''숨겨 놓은 인스턴스 변수 __age의 값을 받아오는 메소드'''
        return self._age

    def set_age(self, value):
        '''숨겨 놓은 인스턴스 변수 __age의 값을 설정하는 메소드'''
        if value < 0:
            print('나이는 0보다 작을 수 없습니다. 기본 값 0으로 나이를 설정하겠습니다.')
            self._age = 0
        else:
            self._age = value

    def __str__(self):
        '''주민 정보를 문자열로 리턴하는 메소드'''
        return f'{self.name}씨는 {str(self._age)}살 입니다!'


osh = Citizen('oshmos', 26, '12345678')
print(osh._age)
print(osh._resident_id)

