import sys

t = int(input())
for i in range(t):
    n, m = map(int, sys.stdin.readline().split())
    printer = list(map(int, sys.stdin.readline().split()))

    head, tail, counter = 0, len(printer), 1
    flag = True
    k = 0
    while True:
        cur = printer[head]
        if cur == max(printer[head:]):
            if head == m:
                print(counter)
                break
            else:
                counter += 1
                head += 1
        else:
            if head == m:
                m += tail - head
            printer.append(cur)
            head += 1
            tail += 1
