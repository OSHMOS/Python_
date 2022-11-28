minguk = list(map(int, input().split()))
manse = list(map(int, input().split()))
if sum(minguk) > sum(manse):
    print(sum(minguk))
elif sum(minguk) < sum(manse):
    print(sum(manse))
else:
    print(sum(manse))
