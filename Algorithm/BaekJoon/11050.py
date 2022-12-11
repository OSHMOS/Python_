def f(n):  # factorial
    ans = 1
    for i in range(2, n+1):
        ans *= i
    return ans


def bino_coef_f(n, k):  # 이항계수
    return f(n) // f(k) // f(n - k)


n, k = map(int, input().split())  # sys를 import해도 걸리는 시간은 동일
print(bino_coef_f(n, k))
