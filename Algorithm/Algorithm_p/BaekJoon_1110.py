input_str = input()
input_sum = 0
cycle = 0

if int(input_str) < 10:
    input_str = "0" + input_str

input_num = input_str

i = 0

while i <= 2:
    input_sum += int(input_str[i])
    i += 1

    if i == 1:
        input_sum += int(input_str[i])
        if input_sum >= 10:
            input_sum -= 10
        input_str = input_str[-1] + str(input_sum)
        cycle += 1

    if i == 2:
        input_sum = 0
        i = 0

    if input_num == input_str:
        break

print(cycle)


