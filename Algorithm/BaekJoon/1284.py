while True:
    result = 0
    ipt_list = input()
    if int(ipt_list) == 0:
        break
    for i in ipt_list:
        if i == '1':
            result += 2
        elif i == '0':
            result += 4
        else:
            result += 3
    result += len(ipt_list) + 1
    print(result)
