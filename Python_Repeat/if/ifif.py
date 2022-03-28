# 중첩 if문 첫 번째 형태
num = int(input("숫자를 입력하시오. "))
if num > 100:
    if num < 1000:
        print("100보다 크고 1000보다 작군요.")
    else:
        print("와~ 1000보다 크군요.")
else:
    print("음~ 100보다 작군요.")

# 중첩 if문 두 번째 형태
score = int(input("점수를 입력하시오. "))
if score >= 90:
    print("A", end='')
else:
    if score >= 80:
        print("B", end='')
    else:
        if score >= 70:
            print("C", end='')
        else:
            if score >= 60:
                print("D", end='')
            else:
                print("F", end='')
print(" 학점입니다.")