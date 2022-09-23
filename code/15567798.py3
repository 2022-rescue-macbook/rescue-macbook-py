test_case=int(input())
for i in range(test_case):
    N,M=map(int,input().split())
    #가중치 weight
    weight=list(map(int,input().split()))
    #원래 숫자의 순서 num
    num=list(range(1,N+1))
    #출력 순서 order
    order=[]
    #궁금한 숫자
    x=num[M]
    
    while True:
        maximum=max(weight)
        first_num=num[0]
        first_w=weight[0]

        if first_w<maximum:
            num.append(first_num)
            num.pop(0)
            weight.append(first_w)
            weight.pop(0)
        else:
            order.append(first_num)
            num.pop(0)
            weight.pop(0)
            if len(num)==0:
                break
    print (order.index(x)+1)





    


