# 1
A = int(input())
B = int(input())
print(A+B)

# 2
T = int(input())
A = 0
B = 0
for i in range(T):
    A, B = map(int, input().split())
    print(A+B)

# 이진혁님 코드 리뷰
if __name__=="__main__":
    T = int(input())
    for _ in range(T):
        A, B = map(int, input().split())
        while not(0<A<10 and 0<B<10):
            if A < 0 or A > 10:
                A = int(input("A의 범위는 0이상 10이하입니다. 다시 입력해주세요."))
            if B < 0 or B > 10:
                B = int(input("B의 범위는 0이상 10이하입니다. 다시 입력해주세요."))
        print(A+B)