#1933/ 프린터 큐
import sys
input=sys.stdin.readline
def find_print(M,imp_list):
    count=0
    max_val=max([i[1] for i in imp_list])
    while True:
        if imp_list[0][1]==max_val: #빠져야함
            if imp_list[0][0]==M:
                return count+1
            else:
                count+=1
                imp_list.pop(0)
                max_val=max([i[1] for i in imp_list])
        else: #안빠져야함
            temp=imp_list[0]
            imp_list=imp_list[1:]
            imp_list.append(temp)
    
      
answer=[]
TOTAL=int(input())
for _ in range(TOTAL):
    N,M=map(int,input().split())
    important=list(map(int,input().split()))
    imp_list=[]
    for i in range(N):
        imp_list.append((i,important[i]))
    answer.append(find_print(M,imp_list))
for a in answer:
    print(a)