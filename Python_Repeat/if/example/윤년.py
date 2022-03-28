# 조건의 순서가 굉장히 중요함을 보여주는 예제
year = int(input("연도를 입력하시오. "))
if year % 4 == 0 and year % 400 == 0:
    print("윤년입니다.")
elif year % 4 == 0 and year % 100 == 0:
    print("평년입니다.")
elif year % 4 == 0:
    print("윤년입니다.")
