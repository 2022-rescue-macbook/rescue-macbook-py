import sys

N = int(sys.stdin.readline())

for i in range(N) :
    N, M = map(int, sys.stdin.readline().split())
    p_list = list(map(int, sys.stdin.readline().split()))

    cnt = 0
    while True :
        if p_list[0] == max(p_list) :
            if M == 0 :
                print(cnt + 1)
                break
            else :
                p_list = p_list[1:]
                cnt += 1
                M -= 1
        else :
            tmp = p_list[0]
            p_list = p_list[1:]
            p_list.append(tmp)
            if M == 0 :
                M = len(p_list) - 1
            else :
                M -= 1