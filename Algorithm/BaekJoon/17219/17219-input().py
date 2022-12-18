N, M = map(int, input().split())
info = {}
for _ in range(N):
    url, pw = input().split()
    info[url] = pw
find_list = [input() for _ in range(M)]
for find in find_list:
    print(info[find])
