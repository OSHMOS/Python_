gx = 100

def myfunc():
  gx = 200 # 전역 변수 gx와 다른 지역 변수 gx
  return gx

print(myfunc())
print(gx)

