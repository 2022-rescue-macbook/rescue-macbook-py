import sys
tc=int(sys.stdin.readline())

def find():
    for j in range(len(n_list)):
        if n_list[0][0]<n_list[j][0]:
            return True
    return False
ans=[]
for i in range(tc):
    n,m=map(int,sys.stdin.readline().split())
    n_list=[[int(x),idx] for idx,x in enumerate(sys.stdin.readline().split())]

    b=n_list[m]
    a=0
    for k in range(n):
        while find():
            n_list.append(n_list[0])
            del n_list[0]
        a+=1
        if n_list[0][1]==b[1]:
            ans.append(a)
            break
        del n_list[0]
for num in ans:
    print(num)