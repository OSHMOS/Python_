# sum_number는 자꾸 number로 초기화가 되는데 어떻게 연산이 유지가 될 수 있는가?
def sum(number):
  if number == 1:
    return 1
  sum_number = number
  sum_number += sum(number - 1)
  return sum_number

def main():
  num = int(input("어떤 수까지 더하고 싶어요?"))
  print(sum(num))

main()