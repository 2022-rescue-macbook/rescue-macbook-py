import sys


T = int(sys.stdin.readline())
i = 0
while i < T:
    N, M = map(int, sys.stdin.readline().split())
    imp_list = list(map(int, sys.stdin.readline().split()))
    target = imp_list[M]
    cnt = 0
    while True:
        if M == 0:
            if target < max(imp_list):
                imp_list.append(target)
                del imp_list[0]
                M = len(imp_list) - 1
            else:
                cnt += 1
                sys.stdout.write(str(cnt) + '\n')
                break
        else:
            if imp_list[0] < max(imp_list):
                imp_list.append(imp_list[0])
                del imp_list[0]
                M -= 1
            else:
                del imp_list[0]
                cnt += 1
                M -= 1
    i += 1