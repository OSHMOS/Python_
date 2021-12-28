from random import randint


def generate_numbers():
    numbers = []

    # 코드를 작성하세요.
    while len(numbers) < 3: # for i in range(3): 로 작성하면 3개가 아니라 2개만 뽑히게 될 수도 있다. 
        new_number = randint(0, 9)
        if new_number not in numbers:
            numbers.append(new_number)

    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers


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

def get_score(guesses, solution):
    strike_count = 0
    ball_count = 0

    # 코드를 작성하세요.
    for i in range(len(solution)):
        if guesses[i] in solution and guesses[i] == solution[i]:
            strike_count += 1
        elif guesses[i] in solution:
            ball_count += 1
        else:
            strike_count += 0
            ball_count += 0

    return strike_count, ball_count


# 여기서부터 게임 시작!
ANSWER = generate_numbers()
tries = 0

print(ANSWER)
# 코드를 작성하세요.
while True:
    new_guess = take_guess()
    s, b = get_score(new_guess, ANSWER)

    print(f"{s}S {b}B")
    tries += 1

    if s == 3:
        break



print(f"축하합니다. {tries}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.")