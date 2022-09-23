def fn(M, In):
    In = [[In[i], i] for i in range(len(In))]
    
    cnt = 1

    while True:
        index = 0
        Max = 0
        for i in range(len(In)):
            if Max < In[i][0]:
                Max = In[i][0]
                index = i

        if In[index][1] == M:
            return cnt
        else:
            cnt += 1
            In = In[index+1:] + In[:index] 

re = int(input())

lst = list()
for i in range(re):
    N, M = map(int, input().split())
    In = list(map(int, input().split()))
    
    a = fn(M, In)
    lst.append(a)

for i in lst:
    print(i)