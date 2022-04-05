# 추상화의 안 좋은 예시
class SomeClass:
    class_variable = 0.02

    def __init__(self, variable_1, variable_2):
        self.variable_1 = variable_1
        self.variable_2 = variable_2

    def method_1(self, some_value):
        self.variable_2 += some_value

    def method_2(self, some_value):
        if self.variable_2 < some_value:
            print("Insufficient balance!")
        else:
            self.variable_2 -= some_value

    def method_3(self):
        self.variable_2 *= 1 + SomeClass.class_variable