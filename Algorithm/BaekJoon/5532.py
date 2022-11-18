input_list = [int(input()) for _ in range(5)]
cntm = 0
cntk = 0
while True:
    cntm += 1
    if input_list[3] * cntm >= input_list[1]:
        break

while True:
    cntk += 1
    if input_list[4] * cntk >= input_list[2]:
        break

if cntm > cntk:
    print(input_list[0] - cntm)
else:
    print(input_list[0] - cntk)
