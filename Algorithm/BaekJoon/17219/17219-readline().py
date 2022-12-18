from sys import stdin
N, M = map(int, stdin.readline().split())
info = {}
for _ in range(N):
    url, pw = stdin.readline().split()
    info[url] = pw
find_list = [stdin.readline().rstrip() for _ in range(M)]
for find in find_list:
    print(info[find])
