T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    s = list(map(int, input().split()))
    lst = [0 for _ in range(n)]
    lst[m] = 1
    cnt = 0
    
    while True:
        if s[0] == max(s):
            cnt += 1
            if lst[0] == 1:
                print(cnt)
                break
            s.pop(0)
            lst.pop(0)
        else:
            s.append(s.pop(0))
            lst.append(lst.pop(0))
            