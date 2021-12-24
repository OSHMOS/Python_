from random import *

n = int(input())
ar = []

for i in range(n):
  a = randint(-100, 100)
  ar.append(a)

def plusMinus(ar):
  plus = 0
  minus = 0
  zero = 0
  for i in range(n):
    if int(ar[i]) > 0:
      plus = plus + 1
    elif int(ar[i]) < 0:
      minus = minus + 1
    elif int(ar[i]) == 0:
      zero = zero + 1
  plusRatio = plus/n
  minusRatio = minus/n
  zeroRatio = zero/n
  return plusRatio, minusRatio, zeroRatio # print(plusRatio, minusRatio, zeroRatio)도 가능

result = plusMinus(ar)
print(result)