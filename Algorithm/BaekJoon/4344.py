test_num = int(input())

for i in range(test_num):
    input_score = list(map(int, input().split()))
    # 처음에 받은 숫자만큼의 리스트 개수를 얻기 위함

    avg = sum(input_score[1:])/input_score[0]
    # 리스트의 0번 인덱싱 값은 점수가 아니기 때문에 1번부터 끝까지 슬라이싱해서 합을 구해야 함
    # 리스트의 세계는 무궁무진함
    cnt = 0

    for score in input_score[1:]:
        if score > avg:
            cnt += 1
    rate = cnt / input_score[0] * 100
    print(f"{rate:.3f}%")
    # 문자열 포맷팅은 확실히 공부하고 사용 중이라서 이제는 익숙함