from random import randint


def generate_numbers(n):
    # 코드를 작성하세요.
    num = []
    for i in range(n):
        a = randint(1, 45)
        num.append(a)
    return num


def draw_winning_numbers():
    # 코드를 작성하세요.
    num = generate_numbers(6)
    num = sorted(num)
    bonus_num = randint(1, 45)
    num.append(bonus_num)
    return num


def count_matching_numbers(numbers, winning_numbers):
    # 지난 과제의 코드를 붙여 넣으세요.
    count = 0
    for num in numbers:
        if num in winning_numbers:
            count += 1
    return count


def check(numbers, winning_numbers):
    # 코드를 작성하세요.
    special_count = count_matching_numbers(numbers, winning_numbers[6:])
    count = count_matching_numbers(numbers, winning_numbers[:6])
    if count == 6:
        return 1000000000
    elif count == 5 and special_count == 1:
        return 50000000
    elif count == 5:
        return 1000000
    elif count == 4:
        return 50000
    elif count == 3:
        return 5000
    else:
        return 0

