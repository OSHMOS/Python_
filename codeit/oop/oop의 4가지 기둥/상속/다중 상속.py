# 엔지니어 클래스
class Engineer:
    def __init__(self, favorite_language):
        self.favorite_language = favorite_language

    def program(self):
        print(f'{self.favorite_language}(으)로 프로그래밍합니다.')

# 테니스 선수 클래스
class TennisPlayer:
    def __init__(self, tennis_level):
        self.tennis_level = tennis_level

    def play_tennis(self):
        print(f'{self.tennis_level} 반에서 테니스를 칩니다.')

'''
다중 상속의 단점
다중 상속으로 받았을 때
super()가 어떤 클래스를 가리키는 지 알 수가 없다.
'''
class EngineerTennisPlayer(Engineer, TennisPlayer):
    def __init__(self, favorite_language, tennis_level):
        Engineer.__init__(self, favorite_language)
        TennisPlayer.__init__(self, tennis_level)

# 다중 상속을 받는 클래스의 인스턴스 생성
younghoon = EngineerTennisPlayer('파이썬', '초급')

# 두 부모 클래스의 메소드들을 잘 물려받았는지 확인
younghoon.program()
younghoon.play_tennis()