# 1966
import sys
testCase = int(input())

for _ in range( testCase ):
    priority = {key : [] for key in range(9, 0, -1)}
    
    N, M = list(map(int, input().split()))
    if N < 1:
        print( 0 )
        continue
    
    datas = list(map(int, input().split()))
    target = datas[M]
    for i, data in enumerate(datas):
        priority[data].append( i )
    
    topPriority = max(datas)

    index = priority[ topPriority ][ 0 ] 
    
    num = 0
    for key in range( topPriority, 0, -1 ):
        if len( priority[key] ) == 0:
            continue
        elif key == target:
            break
        else:
            num += len( priority[key] )
            
            x = [i for i in priority[key] if i<index]
            if x == []:
                index = priority[key][-1]
            else:
                index = x[-1]
    
    x = [i for i in priority[key] if i<index]
    y = [i for i in priority[key] if i>=index]
    if index > M:
        num += len(y)
        num += x.index( M ) + 1
    else:
        num += y.index( M ) + 1
        
    print( num )