num = int(input())
cnt = num
for i in range(num):
    voca = input()
    for j in range(len(voca) - 1):
        if voca[j] == voca[j+1]:
            pass
        elif voca[j] in voca[j+1:]:
            cnt -= 1
            break
print(cnt)