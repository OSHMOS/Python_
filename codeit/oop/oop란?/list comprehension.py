# int_list = [1, 2, 3, 4, 5, 6]
# squares = []

# for x in int_list:
#     squares.append(x**2)

# print(squares) # [1, 4, 9, 16, 25, 36]

int_list = [1, 2, 3, 4, 5, 6]
squares = [x**2 for x in int_list]

print(squares) # [1, 4, 9, 16, 25, 36]