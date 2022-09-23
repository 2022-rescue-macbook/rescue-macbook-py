lst=[]
Plst=[]
testCase=int(input())
temp=0

for i in range(testCase):
    count=0
    DocNum, finNum=input().split()
    DocNum=int(DocNum)
    finNum=int(finNum)
    lst=input().split()
    lst2=lst.copy()
    lst2.sort()
    lst2.reverse()
    Plst.clear()
    for j in range(DocNum):
        if j==finNum:
            Plst.append(1)
        else:
            Plst.append(0)
    while True:
        if lst[0]==lst2[0]:
            count+=1
            del(lst[0])
            del(lst2[0])
            if Plst[0]==1:
                print(count)
                break
            del(Plst[0])
        else:
            temp=lst[0]
            del(lst[0])
            lst.append(temp)
            temp=Plst[0]
            del(Plst[0])
            Plst.append(temp)
