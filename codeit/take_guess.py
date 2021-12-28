def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")

    new_guess = []
    # 코드를 작성하세요.
    i = 1
    while i < 4:
        num = int(input(f"{i}번째 숫자를 입력하세요: "))
        if num in new_guess:
            print("중복되는 숫자입니다. 다시 입력하세요.")
            i -= 1
        if num > 9:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
            i -= 1
        else:
            new_guess.append(num)
        i += 1
    return new_guess


print(take_guess())