with open("vocabulary.txt", "a") as file:
    while True:  # line이 file에 존재하지 않습니다.
        voca = input("영어 단어를 입력하세요: ")
        if voca == "q":
            break
        mean = input("한국어 뜻을 입력하세요: ")
        if mean == "q":
            break

        file.write(f"{voca}: {mean}\n")