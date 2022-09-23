import sys
input=sys.stdin.readline

t=int(input())

for i in range(t):
    n,m=map(int,input().split())
    print_list=list(map(int,input().split()))
    chk_list=[0 for _ in range(n)]
    chk_list[m]=1
    count = 0

    while True:
        if print_list[0]==max(print_list):
            count+=1

            if chk_list[0]!=1:
                del print_list[0]
                del chk_list[0]
            else:
                print(count)
                break
        else:
            print_list.append(print_list[0])
            chk_list.append(chk_list[0])
            del print_list[0]
            del chk_list[0]
