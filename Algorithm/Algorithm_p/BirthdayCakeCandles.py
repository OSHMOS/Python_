from random import *

n = int(input())
arr = []

for i in range(n):
  a = randint(1,10000000)
  arr.append(a)

def birthdayCakeCandles(arr):
  return arr.count(max(arr))

result = birthdayCakeCandles(arr)
print(result)

# python에서 사용하는 자체적인 함수를 많이 알아두자!