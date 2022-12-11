import sys
N = int(sys.stdin.readline())
base_list = [0] * 10000

for i in range(N):
    input_num = int(sys.stdin.readline())

    base_list[input_num - 1] = base_list[input_num - 1] + 1

for i in range(10000):
    if base_list[i] != 0:
        for j in range(base_list[i]):
            print(i + 1)
