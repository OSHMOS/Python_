# word = input()

# # dž는 무조건 하나의 알파벳으로 쓰이고,
# # d와 ž가 분리된 것으로 보지 않는다고 했으므로
# # z=보다 dz=를 먼저 써야 함.
# word = word.replace('c=', 'q')
# word = word.replace('c-', 'w')
# word = word.replace('dz=', 'e')
# word = word.replace('d-', 'r')
# word = word.replace('lj', 't')
# word = word.replace('nj', 'y')
# word = word.replace('s=', 'u')
# word = word.replace('z=', 'i')

# print(len(word))
# 위의 방식이 가장 효율적인 것은 맞는데
# 정리만 하면 코드가 이쁠 것 같아서
# 정리를 해보면
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in croatia:
    word = word.replace(i, '*')
print(len(word))
