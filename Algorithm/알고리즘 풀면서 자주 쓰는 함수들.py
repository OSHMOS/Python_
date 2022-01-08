### find(찾을 문자, 찾기 시작할 위치)
# find는 문자열 중에 특정 문자를 찾고 해당 위치를 반환. 없을 경우 -1을 반환.
sentence = 'this is a sentence'

print(sentence.find('a'))  # 8
print(sentence.find('d'))  # -1
print(sentence.find('a', 9))  # -1

### startswith(시작하는 문자, 시작 지점)
# startswith는 문자열이 특정 문자로 시작하는지 여부를 알려준다.
# true나 false 를 반환
# 두 번째 인자를 넣음으로써 찾기 시작할 지점을 정할 수 있다.
sentence = 'this is a sentence'

print(sentence.startswith('t'))  # True
print(sentence.startswith('a'))  # False

### endswith(끝나는 문자, 문자열의 시작, 문자열의 끝)
# endswith는 문자열이 특정 문자로 끝나는지 여부를 알려준다.
# true나 false를 반환
# 두 번째 인자로 문자열의 시작과 세 번쨰 인자로 문자열의 끝을 지정할 수 있다.
sentence = 'this is a sentence'

print(sentence.endswith('e'))  # True
print(sentence.endswith('c'))  # False
print(sentence.endswith('a', 0, 9))  # True
print(sentence.endswith('a', 0, 7))  # False

### sort(), sorted()
array1 = [2, 11, 4, 5, 9]
array1.sort()  # sort()는 원래 배열 자체를 정렬한다.
print(array1)

array2 = [2, 12, 6, 3, 8]
new_array = sorted(array2)  # sorted()는 원래 배열의 복사본을 정렬해서 다른 이름을 지어준다.
print(array2)
print(new_array)

### reverse(), reversed()
array1.reverse()  # 현재 array1은 [2, 4, 5, 9, 11]
print(array1)  # reverse()는 단순히 역순으로 정렬한다.

rev_array2 = reversed(array2)
print(array2)
print(rev_array2)
print(list(rev_array2))


