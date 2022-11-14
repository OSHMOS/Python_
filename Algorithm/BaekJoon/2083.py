while True:
    students = list(input().split())
    if students == ['#', '0', '0']:
        break
    if int(students[1]) > 17 or int(students[2]) >= 80:
        print(f'{students[0]} Senior')
    else:
        print(f'{students[0]} Junior')
