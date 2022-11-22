mo = ['a', 'i', 'e', 'o', 'u', 'A', 'I', 'E', 'O', 'U']
while True:
    cnt = 0
    sentence = input()
    if sentence == '#':
        break
    for i in sentence:
        if i in mo:
            cnt += 1
    print(cnt)
