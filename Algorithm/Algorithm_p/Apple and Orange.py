s = int(input())
t = int(input())
a = int(input())
b = int(input())
m = int(input())
n = int(input())
apples = []
oranges = []

for i in range(m):
  a = int(input())
  apples.append(a)

for i in range(n):
  o = int(input())
  oranges.append(o)

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    finalAP = 0
    finalOP = 0
    for i in range(m):
        AP = a + (apples[i])
        if AP >= s and t >= AP:
            finalAP = finalAP + 1
    for i in range(n):
        OP = b + (oranges[i])
        if OP >= s and t >= OP:
            finalOP = finalOP + 1
    print(finalAP)
    print(finalOP)

result = countApplesAndOranges(s, t, a, b, apples, oranges)
print(result)

# 이때부터 문제가 이해되는 순간부터 깔끔하게 풀려가는 느낌이 들기 시작했다.