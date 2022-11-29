# 대응 => 딕셔너리
octo_dic = {'-': 0, '\\': 1, '(': 2, '@': 3,
            '?': 4, '>': 5, '&': 6, '%': 7, '/': -1}
while True:
    result = 0
    octo = input()
    if octo == '#':
        break
    for i in range(len(octo)):
        result += octo_dic[octo[i]] * 8 ** (len(octo) - i - 1)
    print(result)
