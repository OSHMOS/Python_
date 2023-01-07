from math import factorial
n, m = map(int, input().split())
up = factorial(n)
down = factorial(m) * factorial(n - m)
print(up // down)
