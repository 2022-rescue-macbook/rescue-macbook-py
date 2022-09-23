import sys
input = sys.stdin.readline


def Print(N, M, Imp):
    count = 0

    while True:
        if Imp[0] == max(Imp):
            Imp.pop(0)
            count += 1
            if M == 0:
                break
            else:
                M -= 1
        else:
            Imp.append(Imp.pop(0))
            if M == 0:
                M = len(Imp) - 1
            else:
                M -= 1

    return count


K = int(input())

for i in range(K):
    N, M = map(int, input().split())
    Imp = list(map(int, input().split()))
    print(Print(N, M, Imp))
