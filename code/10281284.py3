import sys

N = int(sys.stdin.readline().strip("\n"))

for n in range(N):
    size, target = sys.stdin.readline().split()
    printerQueue = sys.stdin.readline().split()
    size = int(size)
    target = int(target)

    # (value, index) tuple
    order = list(zip(printerQueue, [n for n in range(size)]))
    count = 0
    while True:
        if printerQueue[0] == max(printerQueue):
            count += 1
            if order[0][1] == target:
                sys.stdout.write(str(count) + "\n")
                break
            else:
                order.pop(0)
                printerQueue.pop(0)
        else:
            order.append(order.pop(0))
            printerQueue.append(printerQueue.pop(0))