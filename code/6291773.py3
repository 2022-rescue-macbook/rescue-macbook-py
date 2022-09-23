t=int(input())
for _ in range(t):
    n, m = map(int,input().split())
    queue = list(map(int,input().split()))
    count = 0
    while( True ):
        count += 1
        max_index = queue.index(max(queue))
        if ( queue[m] == max(queue) ):
            if ( m != max_index ):
                count += queue[:m].count(queue[m])
            break
        else:
            queue = queue[max_index:]+queue[:max_index]
            if ( max_index < m ):
                m -= max_index + 1
            elif ( m < max_index ):
                m += len(queue) - max_index - 1
            queue.pop(0)
    print(count)