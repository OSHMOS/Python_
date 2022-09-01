price = int(input())
N = int(input())
m_list = []
for i in range(N):
    num_list = list(map(int, input().split()))
    m_list.append(num_list[0] * num_list[1])
if price == sum(m_list):
    print('Yes')
else:
    print('No')
