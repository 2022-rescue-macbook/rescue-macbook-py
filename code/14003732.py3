testcase = int(input())
while(testcase):
    N,M = map(int, input().strip().split())
    que = list(map(int , input().strip().split()))
    cnt = 0
    target = M  #M은 que 에서 인덱스처럼 사용. 계속 변하게 될 것.
    flag=  True
    while(flag):
        MAX = max(que)
        if(que[target] ==MAX and target ==0):
            del que[0]
            cnt +=1
            flag= False
        else:
            # 타겟 데이터가 맨 뒤로 옮겨졌을 때.
            if( que[0] != MAX and target ==0):
                que.append(que[0])
                del que[0]
                target = len(que)-1
            #다른 원소가 자신의 뒤로 올 때.
            if(que[0] != MAX and  target !=0):
                que.append(que[0])
                del que[0]
                target -=1
            #MAX 값 원소가 pop 될 때.
            if(que[0] == MAX and target !=0):
                del que[0]
                target -=1
                cnt +=1
    print(cnt)
    testcase -=1
