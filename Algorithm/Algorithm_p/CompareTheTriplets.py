ar = []
a1, a2, a3 = input().split(',')
ar.append(a1)
ar.append(a2)
ar.append(a3)

br = []
b1, b2, b3 = input().split(',')
br.append(b1)
br.append(b2)
br.append(b3)


def compareTriplets(ar, br):
    score = [0, 0]
    for i in range(3):
        if int(ar[i]) > int(br[i]):
            score[0] = score[0] + 1
        elif int(ar[i]) < int(br[i]):
            score[1] = score[1] + 1
    return score
