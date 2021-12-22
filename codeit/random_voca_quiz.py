import random

with open("vocabulary.txt","r") as file:
    line_data_list = []
    for line in file:
        line_data = line.strip().split(": ")
        line_data_list.append(line_data[1])

with open("vocabulary.txt","r") as file:
    for line in file:
        answer = input(f"{line_data_list[random.randint(0, 7)]}: ")
        # line_data_list의 append 작업을 끝내지 않으면 index가 out of range일 수 있다.
        # random이기 때문이다.
        if answer == "q":
            break

        if answer == line_data[0]:
            print("맞았습니다!")
        else:
            print(f"아쉽습니다. 정답은 {line_data[0]}입니다.")
