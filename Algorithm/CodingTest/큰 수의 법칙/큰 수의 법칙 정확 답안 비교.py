import time

# 프로그램 소스코드
# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

start_time = time.time()
data.sort() # 입력받은 수 정렬
first = data[n - 1] # 가장 큰 수
second = data[n - 2] # 두 번째로 큰 수

# 요 부분이 아직도 이해가 되지 않아요.
# 이해는 했는데 내가 과연 이 문제를 다음에 볼 때 이 생각을 할 수 있을지...
# 가장 큰 수가 더해지는 횟수 계산
count = m // (k + 1) * k
count += m % (k + 1)

result = 0
result += (count) * first # 가장 큰 수 더하기
result += (m - count) * second # 두 번째로 큰 수 더하기

print(result)

end_time = time.time()
print(f"time : {end_time - start_time}")