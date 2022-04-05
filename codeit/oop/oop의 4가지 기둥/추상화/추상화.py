# type hinting (강제성 X)
class BankAccount:
    '''은행 계좌 클래스'''
    interest: float = 0.02

    def __init__(self, owner_name: str, balance: float): # 함수의 header
        '''인스턴스 변수 : name(문자열), balance(실수형)''' # 함수의 body 시작
        self.owner_name = owner_name # 함수의 body
        self.balance = balance

    def deposit(self, amount: float) -> None:
        '''잔액 인스턴스 변수 balance를 파라미터 amount만큼 늘려주는 메소드'''
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        '''잔액 인스턴스 변수 balance를 파라미터 amount만큼 줄여주는 메소드'''
        if self.balance <  amount:
            print("Insufficient balance!")
        else:
            self.balance -= amount

    def add_interest(self) -> None:
        '''잔액 인스턴스 변수 balance를 이자율만큼 늘려주는 메소드'''
        self.balance *= 1 + BankAccount.interest

bank_account = BankAccount('oshmos', '1000')
# type hinting에 맞지 않게 넣어도 코드가 실행되기는 한다.

print(bank_account.balance) # 1000
bank_account.deposit('00')
print(bank_account.balance) # 100000
