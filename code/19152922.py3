cases = int(input())

for c in range(cases):
    N, M = map( int , input().split() )
    q = list(map( int, input().split() ))
    
    m_idx = M; loop = 0
    
    while(len(q) != 0):
        loop += 1
        for i in q[0:q.index(max(q))]:
            q.append(q.pop(q.index(i)))
            #print(q)
            if m_idx == 0:
                m_idx = len(q)-1
            else :
                m_idx -= 1
            #print(m_idx)

            
        if m_idx == 0:
            cnt = loop
            #print('cnt')
                    
        q.pop(0)
        m_idx -= 1
        #print('end')
    print(cnt)