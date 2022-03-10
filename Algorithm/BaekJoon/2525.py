A, B = map(int, input().split())
time = int(input())
B += time

if B >= 60:
    A += B//60
    B %= 60

if A >= 24:
    A -= 24
    
print(A, B)

