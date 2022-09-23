N= int(input())
while(N!=0):
    N-=1
    n,m=map(int,input().split())
    print_list = list(map(int,input().split()))
    prior_number=[]

    for i in print_list:
        prior_number.append(i)
    
    result=[0 for _ in range(n)]
    queue=[i for i in range(n)]
    sequence =1
    while queue:
        if print_list[queue[0]]== max(prior_number):
            prior_number.remove(max(prior_number))
            result[queue.pop(0)]=sequence
            sequence+=1
        else:
            queue.append(queue.pop(0))
    print(result[m])