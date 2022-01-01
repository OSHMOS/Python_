S = input()
alpha_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in alpha_list:
    if i in S:
        print(S.index(i))  # S라는 인덱싱 가능한 객체에서 i라는 요소가 있는 인덱스의 값을 반환
    else:
        print(-1)