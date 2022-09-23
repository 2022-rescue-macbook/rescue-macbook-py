t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    p = list(map(int, input().split()))
    s = []
    for i in range(n):
        s.append(i)
    count = 0
    while True:
        if p[0] == max(p):
            count +=1    
            if s[0] == m:
                print(count)
                break
            else:
                del s[0]
                del p[0]
        else:
            p.append(p[0])
            del p[0]
            s.append(s[0])
            del s[0]
