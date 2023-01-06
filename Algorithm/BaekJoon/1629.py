from sys import stdin
abc = list(map(int, stdin.readline().rstrip().split()))


def DC(a, b, c):
    if b == 0:
        return 1 % c

    if b == 1:
        return a % c

    x = DC(a, b // 2, c)

    if b % 2 == 0:
        return (x ** 2) % c
    else:
        return ((x ** 2) * a) % c


print(DC(abc[0], abc[1], abc[2]))
