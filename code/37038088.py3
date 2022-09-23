import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N, M = map(int, input().split())
    seq = list(map(int, input().split()))

    cnt = 0
    while seq:
        Max = max(seq)
        M -= 1
        Pop = seq.pop(0)

        if Max != Pop:
            seq.append(Pop)
            if M < 0:
                M = len(seq) - 1

        else:
            cnt += 1
            if M == -1:
                print(cnt)
                break
