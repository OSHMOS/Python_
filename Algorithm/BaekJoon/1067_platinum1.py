N = int(input())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))
result = []


def c_move(l):
    l.insert(0, l[-1])
    l.pop()


while True:
    if X == X:
        break
    c_move(X)

# print(max(result))
