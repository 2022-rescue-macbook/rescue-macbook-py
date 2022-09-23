#1966

t = int(input())
for _ in range(t):
    N, M = map(int, input().split())
    temp = [[i, n] for n,i in enumerate(map(int,input().split()))]
    i = 0
    max_ = max(temp,key = lambda x: x[0])
    while True:
        if temp[0][0] < max_[0]:
            temp.append(temp.pop(0))
        else:
            i += 1
            if temp.pop(0)[1] == M:
                break
            max_ = max(temp,key = lambda x: x[0])
    print(i)     