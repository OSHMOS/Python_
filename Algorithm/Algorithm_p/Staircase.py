n = int(input())

def staircase(n):
  for i in range(1,n+1):
    print( (' '*(n-i) + '#'*i)) # 작은 따옴표 안에 공간이 없으면 있으나 마나하다.
    # print(('#'*i).rjust(n))
  

result = staircase(n)
print(result)