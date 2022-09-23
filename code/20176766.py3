import sys
from _collections import deque
read = sys.stdin.readline

n = int(read())
for _ in range(n):
    size, index = map(int,read().split())
    priority = list(map(int,read().split()))
    pair_v = deque(priority)
    priority.sort()
    priority = deque(priority)

    pair_i = deque([i for i in range(size)])


    result = 0
    #print("\n\npriority : ", priority)
    #print( "pair_v : ", pair_v )
    #print("pair_i: ", pair_i)
    #print(len(priority))
    while len(priority) != 0:
     #   print("\npriority : ", priority)
     #   print("pair_v : ", pair_v)
     #   print("pair_i: ", pair_i)
        if priority[-1] == pair_v[0]:
            if pair_i[0] == index:
                print(result+1)
            pair_v.popleft()
            pair_i.popleft()
            priority.pop()
            result +=1

        else:
            tmpV = pair_v.popleft()
            tmpI = pair_i.popleft()
            pair_v.append(tmpV)
            pair_i.append(tmpI)





