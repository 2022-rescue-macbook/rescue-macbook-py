T = int(input())

for x in range(0,T):
    N, M = map(int, input().split())
    printer_queue = list(map(int,input().split()))
    ct = 0
    while True:
        k = 0
        for m in printer_queue:
            if m > printer_queue[0]:
                k = 1
                break
        if k:
            printer_queue.append(printer_queue[0])
            del printer_queue[0]
            if M == 0:
                M = len(printer_queue)-1
            else:
                M -= 1
        else:
            if M == 0:
                ct += 1
                print(ct)
                break
            else:
                ct += 1
                del printer_queue[0]
                M -= 1