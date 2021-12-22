s = input()
ar = []

def timeConversion(s):
  AM_PM = s[-2:]
  s = s[:8]
  hh, mm, ss = [int(x) for x in s.split(":")]

  if AM_PM == 'PM' and hh != 12:
      return('{:02}:{:02}:{:02}'.format(hh+12, mm, ss))
  elif AM_PM == 'AM' and hh == 12:
      return('{:02}:{:02}:{:02}'.format(0, mm, ss))
  else:
      return('{:02}:{:02}:{:02}'.format(hh, mm, ss))

result = timeConversion(s)
print(result)

# 공통적인 조건은 따로 묶는 것이 좋다.
# format()에 대해서 공부하자!