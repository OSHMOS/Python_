# str_dial = input()
# list_dial = list(str_dial)

# for i in range (len(str_dial)):
#     if 65 <= ord(list_dial[i]) <= 67:
#         list_dial[i] = 3
#     elif 68 <= ord(list_dial[i]) <= 70:
#         list_dial[i] = 4
#     elif 71 <= ord(list_dial[i]) <= 73:
#         list_dial[i] = 5
#     elif 74 <= ord(list_dial[i]) <= 76:
#         list_dial[i] = 6
#     elif 77 <= ord(list_dial[i]) <= 79:
#         list_dial[i] = 7
#     elif 80 <= ord(list_dial[i]) <= 83:
#         list_dial[i] = 8
#     elif 84 <= ord(list_dial[i]) <= 86:
#         list_dial[i] = 9
#     elif 87 <= ord(list_dial[i]) <= 90:
#         list_dial[i] = 10

# print(sum(list_dial))
# word = input()
# sum = 0
# for i in word:
#     if i in ['A', 'B', 'C']:
#         sum += 3
#     elif i in ['D', 'E', 'F']:
#         sum += 4
#     elif i in ['G', 'H', 'I']:
#         sum += 5
#     elif i in ['J', 'K', 'L']:
#         sum += 6
#     elif i in ['M', 'N', 'O']:
#         sum += 7
#     elif i in ['P', 'Q', 'R', 'S']:
#         sum += 8
#     elif i in ['T', 'U', 'V']:
#         sum += 9
#     elif i in ['W', 'X', 'Y', 'Z']:
#         sum += 10

# print(sum)
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
word = input()
sum = 0
for i in range(len(word)):
    for j in dial:
        if word[i] in j:
            sum += dial.index(j) + 3
print(sum)
