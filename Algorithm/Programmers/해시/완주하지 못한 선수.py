# completion은 딕셔너리로 할 필요 없다.
# 어차피 출력은 1개다.
# participant만 딕셔너리로 변환할 때, 키 -> 개수, 값 -> 이름으로 만들고
# 키 그러니까 개수가 1이 아닌 것의 값을 출력하면 된다.
# 요행이라고도 생각은 되나 문제 조건 상 그 편이 훨씬 효율적이다.
### 요행이라서 걸러졌다. ㅎㅎ
# 위의 상황은 중복값이 participant에 있는 경우


# participant = list(input().split())
# completion = list(input().split())
# part_dict = {i : 0 for i in participant}
#
# # 중복값이 없는 경우 : 배열로도 충분하다.
# for i in participant:
#     if i not in completion:
#         answer = i
#
# print(answer)
#
# # 중복값이 있는 경우 : 특히 count()를 써야 한다.
# for i in participant:
#     if i in participant:
#         part_dict[i] += participant.count(i)
#         if part_dict[i] > 1:
#             answer = i
# print(part_dict)

# def solution(participant, completion):
#     answer = ''
#     part_dict = {i : 0 for i in participant}
#     for i in participant:
#         if i not in completion:
#             answer = i
#         if i in participant:
#             part_dict[i] += participant.count(i)
#             if part_dict[i] > 1:
#                 answer = i
#     return answer

# 딕셔너리를 사용할 필요가 없었다.
participant = list(input.split())
completion = list(input.split())

participant.sort()
completion.sort()
completion.append('0')

for i in range(len(participant)):
    if participant[i] != completion[i]:
        answer = participant[i]
        break

print(answer)