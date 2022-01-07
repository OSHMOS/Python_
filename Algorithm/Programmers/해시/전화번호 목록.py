# phone_book = list(input().split())
# answer = True
# phone_book.sort()
# print(phone_book)
# ['119', '1195524421', '97674223']
# 하하하 알아서 정렬시켜준다 하하하
# 그럼 첫번째랑 그 다음 것만 비교해보고 기면 false 아니면 true라고 생각해도 된다.

phone_book = list(input().split())
answer = True
phone_book.sort()
for i in range(len(phone_book) - 1):
    if phone_book[i+1].startswith(phone_book[i]):
        print(False)
        break # 하나라도 접두어로 포함이 되면 반복문 종료시켜도 된다.(문제 조건상)
    else:
        print(True)

# 해쉬로 푼 풀이(공부용)
# def solution(phone_book):
#     answer = True
#     hash_map = {}
#     for phone_number in phone_book:
#         hash_map[phone_number] = 1
#     for phone_number in phone_book:
#         temp = ""
#         for number in phone_number:
#             temp += number
#             if temp in hash_map and temp != phone_number:
#                 answer = False
#     return answer
