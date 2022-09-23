import sys
input=sys.stdin.readline
case_Num=int(input())
for i in range(case_Num):
    N,M=map(int,input().split())
    case_list=list(map(int,input().split()))
    target_list=list(range(len(case_list)))
    target_list[M]='target_Num'
    order=0
    while True:
        if case_list[0]==max(case_list):
            order+=1
            if target_list[0]=='target_Num':
                print(order)
                break
            else:
                case_list.pop(0)
                target_list.pop(0)
        else:
            case_list.append(case_list[0])
            del case_list[0]
            target_list.append(target_list[0])
            del target_list[0]