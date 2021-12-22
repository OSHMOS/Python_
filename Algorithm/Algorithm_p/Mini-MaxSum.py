from random import *

n = int(input())
arr = []

for i in range(n):
  a = randint(1,1000000000)
  arr.append(a)

def miniMaxSum(arr):
  sum = 0
  arrmin = 0
  arrmax = 0
  for i in range(n):
        sum = sum + arr[i]
        if arr[i-1] < arr[i]:
            arrmax = arr[i]
        elif arr[i-1] > arr[i]:
            arrmin = arr[i]
  print((sum - arrmax), (sum - arrmin))

  # sum = 0
  # arrmin = min(arr)
  # arrmax = max(arr)
  # for i in range(5):
  #     sum = sum + arr[i]
    
  # print((sum - arrmax), (sum - arrmin)) // 이렇게 세상 간단한 방법도 있다.

result = miniMaxSum(arr)
print(result)

# pythondpsms 최댓값, 최솟값 함수가 있다.