while True:
    num = input()
    if num == '0':
        break
    if num == num[::-1]:  # 완벽하게 거꾸로 뒤집는 방법
        print('yes')
    else:
        print('no')
