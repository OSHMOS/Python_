input_list = list(map(int, input().split()))
pair_list1 = sorted(input_list)
pair_list2 = sorted(input_list, reverse=True)
if input_list == pair_list1:
    print('ascending')
elif input_list == pair_list2:
    print('descending')
else:
    print('mixed')
