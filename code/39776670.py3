n = int(input())
for _ in range(n):
    m,ch=map(int,input().split()) # 문서의 개수 / 몇번쨰 나타내는 정수
    l=list(map(int,input().split())) # 문서의 개수 -> 중요도 표시 ex) 문서의 개수 3 -> 중요도 1 2 3
    ch_list=l.copy()
    ch_list.sort()
    i,count=0,0
    while True:
        x=ch_list.pop()
        while True:
            if len(l)<=i:
                i=0
            if x==l[i]:
                l[i]=0
                count+=1
                break
            else:
                i+=1
        if ch == i:
            break
        else:
            i+=1
    print(count)