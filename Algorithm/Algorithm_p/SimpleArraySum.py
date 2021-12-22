from random import *
n = int(input())
ar=[]

for i in range(1,n):
  a = randint(0,1000)
  ar.append(a)

def simpleArraySum(ar):
  x = 0
  for i in range(0,n-1):
    x = x + ar[i]
  return x

result = simpleArraySum(ar)
print(result)