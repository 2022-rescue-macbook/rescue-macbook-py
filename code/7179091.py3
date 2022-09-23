cases = []
nCase = int(input())
for _ in range(nCase):
    N, M = map(int, input().split(' '))
    queue = list(map(int, input().split(' ')))
    cases.append([N, M, queue])
for i in cases:
    M = i[1]
    queue = i[2]
    Mprint = 1
    printed = False
    while printed == False:
        head = queue[0]
        if head >= max(queue):
            if M == 0:
                printed = True
            else:
                M = (M + len(queue) - 1) % len(queue)
                Mprint += 1
                queue.pop(0)
        else:
            M = (M + len(queue) - 1) % len(queue)
            queue.append(queue.pop(0))
    print(Mprint)
