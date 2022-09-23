import sys
input = sys.stdin.readline

a = int(input())

for i in range(a):
    n,m = map(int, input().split())
    infortant = list(map(int,input().split()))
    check = [0] * n
    check[m] = 1
    cnt = 0
    while 1:
        if infortant[0] == max(infortant):
            cnt += 1
            infortant.pop(0)

            if check[0] == 1:
                print(cnt)
                break
            check.pop(0)

        else:
            infortant.append(infortant[0])
            del infortant[0]

            check.append(check[0])
            del check[0]
