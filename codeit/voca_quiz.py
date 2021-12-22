with open("vocabulary.txt","r") as file:
    for line in file:
        line_data = line.strip().split(": ")
        answer = input(f"{line_data[1]}: ")

        if answer == line_data[0]:
            print("맞았습니다!")
        else:
            print(f"아쉽습니다. 정답은 {line_data[0]}입니다.")