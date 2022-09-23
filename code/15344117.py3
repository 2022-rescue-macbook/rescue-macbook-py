
case = int( input() )

result = []

for c in range ( case ):


    NM = list( map(int, input().split(' ') ) )
    N = NM[0]
    M = NM[1]

    priority = list( map(int, input().split(' ') ) )

    queue = []
    for n in range(N): queue.append( n )

    outCount = 0
  
    while len(queue) > 0 :

        v = queue[0]
        p = priority[0]

        isOutput = True
        
        for i in range(1, len(queue)):
            if p < priority[i]:
                isOutput = False

                queue.append( v )
                priority.append( p )

                del queue[0]
                del priority[0]
                break

        if isOutput == True:
            outCount += 1
            del queue[0]
            del priority[0]
            
            if v == M : result.append( outCount )


for n in result:
    print( n )
