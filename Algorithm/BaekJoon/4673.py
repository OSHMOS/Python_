# def d(n):
#     num = list(str(n))
#     for i in range(len(num)):
#         n += int(num[i])
#     return n
#
# num_i = 1
# while num_i <= 10000:
#     if 1 <= d(num_i) <= 10000:
#         continue
#     else:
#         print(num_i)

# 논리는 대충 이러하다.
# 예제 출력을 확인하면서 내 논리가 틀렸음을 깨달았다.
# if 조건이 솔직히 나조차도 무슨 말인지 모른다.

natural_num = set(range(1, 10001))
generated_num = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    generated_num.add(i)

self_num = sorted(natural_num - generated_num)
for i in self_num:
    print(i)