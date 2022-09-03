from curses.ascii import islower


voca = input()
result = ''
for i in voca:
    if i.islower():
        result += i.upper()
    else:
        result += i.lower()
print(result)
