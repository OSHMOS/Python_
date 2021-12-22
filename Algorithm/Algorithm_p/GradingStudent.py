from random import *

n = int(input())
ar = []

for i in range(n):
  a = randint(0, 100)
  ar.append(a)

def gradingStudents(ar):
  finalGrade = []
  for i in range(n):
      if ar[i] >= 38:
          q = ar[i] / 5
          g = (int(q) + 1) * 5
          if g - ar[i] < 3:
              finalGrade.append(int(g))
          else:
              finalGrade.append(ar[i])
      else:
          g = ar[i]
          finalGrade.append(int(g))
  return finalGrade

result = gradingStudents(ar)
print(result)
print(ar)

# 혼자 힘으로 푼 implementation 난이도 문제
