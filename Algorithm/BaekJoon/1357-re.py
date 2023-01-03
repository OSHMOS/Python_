# 다음에 더 좋은 코드로 바꾸자.
a, b = input().split()


def Rev(x):
    x = str(x)
    x = list(x)
    x.reverse()
    x = ''.join(x)
    return int(x)


print(Rev(Rev(a) + Rev(b)))
