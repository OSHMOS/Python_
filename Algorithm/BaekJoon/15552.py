import sys

tries = int(input())
# sys.stdin.readline() 대신 input()을 하는 것이 20ms 정도 더 빠르다.

for i in range(tries):
    num1, num2 = map(int, sys.stdin.readline().rstrip().split())
    # sys.stdin.readline은 맨 끝의 개행문자까지 입력받기 때문에 rstrip()을 추가로 해주는 것이 좋다.
    print(num1 + num2)