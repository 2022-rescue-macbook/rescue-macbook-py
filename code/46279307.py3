import sys
T = int(input())
for _ in range(T):
    M, N = map(int, sys.stdin.readline().split())
    case = sys.stdin.readline().split()
    idx = list(range(len(case)))
    idx[N] = 'target'

    order = 0

    while True:
        if case[0] == max(case):
            order += 1

            if idx[0] == 'target':
                print(order)
                break
            else:
                case.pop(0)
                idx.pop(0)
        else:
            case.append(case.pop(0))
            idx.append(idx.pop(0))
    