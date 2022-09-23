n = int(input())
while n > 0:
    casenum, documentnum  = map(int, input().split())
    queue = [int(x) for x in input().split()]
    sortedqueue = queue[:]
    sortedqueue.sort()
    sortedqueue.reverse()
    while queue != []:
        if(queue[0] == sortedqueue[0]):
            if(documentnum == 0) :
                print(casenum-len(queue)+1)
                break
            queue.pop(0)
            sortedqueue.pop(0)
            documentnum = documentnum - 1
        else :
            goback = queue[0]
            queue.pop(0)
            queue.append(goback)

            if(documentnum == 0):
                documentnum = len(queue)-1
            else:
                documentnum = documentnum - 1
    n = n - 1
        
