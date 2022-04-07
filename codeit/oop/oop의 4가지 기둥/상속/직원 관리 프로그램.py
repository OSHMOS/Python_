class Employee:
    '''직원 클래스'''
    company_name = '코드잇 버거' # 가게 이름
    raise_percentage = 1.03 # 시급 인상률

    def __init__(self, name, wage):
        '''인스턴스 변수 설정'''
        self.name = name # 이름
        self.wage = wage # 시급

    def raise_pay(self):
        '''시급을 인상하는 메소드'''
        self.wage *= self.raise_percentage

    def __str__(self):
        '''직원 정보를 문자열로 리턴하는 메소드'''
        return f'{Employee.company_name} 직원: {self.name}'

class Cashier(Employee):
    pass

class DeliveryMan(Employee):
    pass
'''
상속 관계에 있는 두 클래스가 있을 때,
자식 클래스로 만든 인스턴스는 부모 클래스의 인스턴스이기도 하다는 점을 뜻합니다. 
이 점은 나중에 ‘다형성’이라는 것을 설명할 때 핵심이 되는 원리입니다.
'''
young = Cashier('강영훈', 8900)
print(isinstance(young, Cashier))
print(isinstance(young, DeliveryMan))
print(isinstance(young, Employee))
