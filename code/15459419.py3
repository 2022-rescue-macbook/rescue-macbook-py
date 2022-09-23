a=int(input())
for i in range(0,a):
    b=list(map(int,input().split(" ")))
    queue=list(map(int,input().split(" ")))
    whatfind=b[1] #찾고자하는 항목 index
    i=1
    while True:
        if(queue[0] == max(queue)):
            if(whatfind == 0):
                
                break
            else: #앞의 값 삭제(프린트)
                del queue[0]
                i+=1
                whatfind-=1
        else: #뒤로 이동
            tmp = queue[0]
            del queue[0]
            queue.append(tmp)
            if(whatfind == 0):
                whatfind=len(queue)-1
            else:
                whatfind-=1
    print(i)