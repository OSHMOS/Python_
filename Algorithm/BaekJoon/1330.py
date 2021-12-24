input_num1, input_num2 = map(int, input().split())  # 언패킹

if input_num1 > input_num2:
    print(">")
elif input_num1 < input_num2:
    print("<")
else:
    print("==")
