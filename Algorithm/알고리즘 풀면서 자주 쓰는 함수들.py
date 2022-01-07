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

### reverse(), reversed()

