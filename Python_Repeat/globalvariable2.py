gx = 100

def myfunc():
  global gx # 이 함수 내에서 사용되는 변수 gx는 함수 밖에서 선언된 전역 변수 gx임을 명시함
  gx = 200
  return gx

print(myfunc())
print(gx)