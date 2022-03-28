import random as ran
score = ran.randint(0, 101)
if score >= 90:
    print("장학생")
elif score >= 60:
    print("합격")
else:
    print("불합격")
print("입니다.")