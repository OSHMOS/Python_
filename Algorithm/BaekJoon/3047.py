A, B, C = sorted(map(int, input().split()))
voca = input()
if voca == 'ABC':
    print(A, B, C)
elif voca == 'ACB':
    print(A, C, B)
elif voca == 'BAC':
    print(B, A, C)
elif voca == 'BCA':
    print(B, C, A)
elif voca == 'CAB':
    print(C, A, B)
elif voca == 'CBA':
    print(C, B, A)
