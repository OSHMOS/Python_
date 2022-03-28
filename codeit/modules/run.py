# 스크립트
# 프로그램을 작동시키는 코드를 담은 실행 용도의 파일

# 모듈
# 프로그램에 필요한 변수들이나 함수들을 정의해 놓은 파일
import area

x = float(input('원의 반지름을 입력해 주세요 : '))
print(f'반지름이 {x}인 원의 면적은  {area.circle(x)}입니다.\n')

y = float(input('정사각형의 변의 길이를 입력해 주세요 : '))
print(f'반지름이 {y}인 원의 면적은  {area.square(y)}입니다.\n')

