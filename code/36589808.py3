t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    li = list(map(int, input().split()))
    li_ = [0] * n
    li_[m] = 1
    cnt = 0
    while True:
        if (li[0] == max(li)):
            cnt += 1
            if (li_[0] == 1):
                print(cnt)
                break
            else:
                del li[0]
                del li_[0]
        else:
            li.append(li[0])
            del li[0]
            li_.append(li_[0])
            del li_[0]

#4 2
#li =  [1 2 3 4]    [1,2,3]
#li_ = [0,0,1,0]    [0,0,1]