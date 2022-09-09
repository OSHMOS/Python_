N = int(input())
input_list = []
for _ in range(N):
    input_list.append(int(input()))
if input_list.count(0) > input_list.count(1):
    print('Junhee is not cute!')
else:
    print('Junhee is cute!')
