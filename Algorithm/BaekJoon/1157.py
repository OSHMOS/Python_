word = input().upper()
word_num = {}
for i in range(len(word)):
    if word[i] in word_num:
        word_num[word[i]] += 1
    else:
        word_num[word[i]] = 1
max_values = max(word_num.values())
answer = []
for key, value in word_num.items():
    if value == max_values:
        answer.append(key)

if len(answer) != 1:
    print('?')
else:
    print(answer[0])

# 324ms

# list와 set()함수로 풀기(공부하기)
words = input().upper()
unique_words = list(set(words))  # 입력받은 문자열에서 중복값을 제거

cnt_list = []
for x in unique_words :
    cnt = words.count(x)
    cnt_list.append(cnt)  # count 숫자를 리스트에 append

if cnt_list.count(max(cnt_list)) > 1 :  # count 숫자 최대값이 중복되면
    print('?')
else :
    max_index = cnt_list.index(max(cnt_list))  # count 숫자 최대값 인덱스(위치)
    print(unique_words[max_index])

# 104ms