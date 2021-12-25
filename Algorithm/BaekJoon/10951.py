while True:
    try:
        num1, num2 = map(int, input().split())
        print(num1 + num2)
    except EOFError:  # 입력이 끝나면 끝이 났음을 알아채고 자동으로 while 반복문을 종료시켜줌.
        break