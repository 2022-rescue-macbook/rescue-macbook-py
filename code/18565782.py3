N = input()
#data = [1,1,9,1,1,1]
que=[]
order =0
#n,m = 6,0
for _ in range(int(N)):
    n,m =  list(map(int, input().split()))
    data = list(map(int, input().split()))
    que=[]
    order =0

    for idx, val in enumerate(data):
        que.append((val, idx))
    while True :
        if que[0][0] == max(que)[0]:

            a = que.pop(0)
            order +=1
            if a[1] == m:
                print(order)
                break
        else : 
            que.append(que.pop(0))
    
#if que[0][0] ==max