from sys import stdin
input = stdin.readline
n, k = map(int, input().split())
price = []
cnt = 0
for _ in range(n):
    price.append(int(input()))
price.reverse()
for i in price:
    if i <= k:
        q = k // i
        cnt += q
        k -= i * q
print(cnt)
