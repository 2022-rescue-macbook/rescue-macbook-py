import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    lst = [0] * n
    lst[m] = True
    cnt = 0
    while True:
        if a[0] == max(a):
            cnt += 1
            if lst[0] == True:
                print(cnt)
                break
            else:
                a.pop(0)
                lst.pop(0)
        else:
            a.append((a.pop(0)))
            lst.append((lst.pop(0)))