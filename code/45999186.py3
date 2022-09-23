
import sys

T = int(input())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())

    impo = list(map(int, sys.stdin.readline().split()))

    target_num = impo[M]

    impo[M] = 0
    count = 0

    while True:

        a = impo[0]

        if impo[0] == 0:

            if target_num >= max(impo) or len(impo) == 1:
                count += 1
                break

            else:
                impo.pop(0)
                impo.append(a)


        elif a == max(impo) and a >= target_num:
            impo.pop(0)
            count += 1

        else:
            impo.pop(0)
            impo.append(a)

    print(count)
