num = int(input())
for _ in range(num):
    n, m = map(int, input().split())
    li = list(map(int, input().split()))
    doc = [0]*n
    doc[m]=1
    ans=0
    while sum(doc)!=0:
        if li[0]==max(li):
            li.pop(0)
            doc.pop(0)
            ans+=1
        else:
            li.append(li.pop(0))
            doc.append(doc.pop(0))
    print(ans)