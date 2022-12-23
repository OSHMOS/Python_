while True:
    def_list = list(map(int, input().split()))
    if sum(def_list) == 0:
        break
    def_list.sort()
    if def_list[2]**2 == def_list[0]**2 + def_list[1]**2:
        print('right')
    else:
        print('wrong')
