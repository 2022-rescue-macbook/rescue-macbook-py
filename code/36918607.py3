from sys import stdin

test = int(stdin.readline())

for _ in range(test):
    cnt = 0
    N, M = map(int, stdin.readline().split())
    imp = list(map(int, stdin.readline().split()))
    test = list(range(len(imp)))
    test[M] = 'P'
    while(1):
        if max(imp) == imp[0]:
            cnt += 1
            imp.pop(0)
            if test[0] == 'P':
                print(cnt)
                break
            else:
                test.pop(0)
        else:
            imp.append(imp.pop(0))
            test.append(test.pop(0))