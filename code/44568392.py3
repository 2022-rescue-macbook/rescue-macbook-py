from sys import stdin

x = int(stdin.readline())


for i in range(x):
    cnt = 0
    n, m = map(int, stdin.readline().split())
    imp = list(map(int, stdin.readline().split()))
    ans =[0 for _ in range(n)]
    ans[m] = 999
    while True:
        if imp[0] == max(imp):
            cnt += 1
            if ans[0] == 999:
                print(cnt)
                break
            else:
                del imp[0]
                del ans[0]
        else:
            imp.append(imp[0])
            ans.append(ans[0])
            del imp[0]
            del ans[0]