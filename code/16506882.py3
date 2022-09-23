num = int(input())
for i in range(num):
    c=[]
    count=0
    M , N = map(int, input().split())
    c = list(input().split())
    ans=[0]*M
    ans[N] = 1
    while (1):
        if c.index(max(c)) == 0:
            del c[0]
            count+=1
            if ans[0] == 1:
                print(count)
                break
            else:
                del ans[0]
        else:
            c.append(c[0])
            del c[0]
            ans.append(ans[0])
            del ans[0]



