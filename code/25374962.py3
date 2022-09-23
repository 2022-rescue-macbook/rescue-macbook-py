Test_Case = int(input())
for _ in range(Test_Case) :
    n,m = list(map(int,input().split()))
    Queue = list(map(int,input().split()))
    idx = list(range(len(Queue)))
    idx[m] = 'a'
    # if len(Queue) != n :
    #     print('Wrong!')
    #     Queue =[]
    Printing = int(0)
    while True : 
        if Queue[0] == max(Queue) :
            Printing += 1
            if idx[0] == 'a' :
                print(Printing)
                break
            else :
                Queue.pop(0)
                idx.pop(0)
        else :
            Queue.append(Queue.pop(0))
            idx.append(idx.pop(0))