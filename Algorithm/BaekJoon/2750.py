N = int(input())
input_list = []
for i in range(N):
    num = int(input())
    input_list.append(num)
for i in sorted(input_list):
    print(i)
