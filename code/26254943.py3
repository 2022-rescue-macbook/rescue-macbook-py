from sys import stdin

for _ in range(int(stdin.readline())):
    N, M = map(int, stdin.readline().split())
    argent = list(map(int, stdin.readline().split()))

    check = list(range(len(argent)))
    check[M] = -1

    order = 0
    while True:
        if argent[0] == max(argent):
            order += 1
            if check[0] == -1:
                print(order)
                break
            else:
                argent.pop(0)
                check.pop(0)
        else:
            argent.append(argent.pop(0))
            check.append(check.pop(0))
