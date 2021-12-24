def kangaroo(x1, v1, x2, v2):
    # Write your code here
    while True:
        x1 = x1 + v1
        x2 = x2 + v2
        
        if x1 == x2:
            return "YES"
        elif (x1 > x2 and v1 >= v2) or (x2 > x1 and v2 >= v1):
            return "NO"

# 반복문을 무한대로 돌리고 싶다 -> whilt True:를 사용하면 된다.
# 선발 주자가 후발 주자보다 앞설 때, 둘의 속도가 같거나 앞선다면, 후발 주자는 선발 주자를 따라올 수 없다.