import sys

def flow(Q, Q2):
    M = max(Q)
    while (True):
        index = Q2.pop(0)
        item = Q.pop(0)

        if M is item:
            break

        Q.append(item)
        Q2.append(index)

    return index, item

T = int(input())
for _ in range(T):
    n, m = map(int, sys.stdin.readline().split())
    test_case = list(map(int, sys.stdin.readline().split()))
    index_list = list(range(len(test_case)))

    num = 0
    while(True):
        i, j = flow(test_case, index_list)
        num += 1
        if i == m:
            break

    print(num)