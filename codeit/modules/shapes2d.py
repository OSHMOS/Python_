PI = 3.14
# 원 클래스
class Circle:
    def __init__(self, radius):
        self.radius = radius


    def area(self):
        return PI * self.radius ** 2

# 정사각형 클래스
class Square:
    def __init__(self,length):
        self.length = length

    def area(self):
        return self.length ** 2