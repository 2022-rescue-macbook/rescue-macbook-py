import sys
for x in range(int(input())):
    n, m = map(int, sys.stdin.readline().split())
    printerque = [int(x) for x in sys.stdin.readline().split()]
    count = 0
    while printerque:
        if printerque[0] < max(printerque):
            printerque.append(printerque.pop(0))
            m = (m - 1 + len(printerque)) % len(printerque)
        elif printerque.index(max(printerque)) == m:
            count = count + 1
            break
        else:
            printerque.pop(0)
            count = count + 1
            m = m - 1
    print(count)
