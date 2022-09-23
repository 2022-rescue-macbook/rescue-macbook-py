a = int(input())
for i in range(a):
    n, m = map(int, input().split())
    s = list(map(int, input().split()))
    count = 0
    flag = True
    while flag:
        f = s[0]
        if f == max(s):
            count+=1
            if m == 0:
                print(count)
                flag = False
            else:
                m-=1
            s.pop(0)
        else:
            s.append(s.pop(0))
            if m==0:
                m = len(s)-1
            else:
                m-=1