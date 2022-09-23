def prioprint(quelen, target, queue):
    count=0
    targetinde=target
    for i in range(9,0,-1):
        for j in range(0,queue.count(i)):
            count += 1
            hiprio=queue.index(i)
            # for debug
            # print(queue)
            # print(targetinde)
            # print(hiprio)
            # print(count)
            if hiprio==targetinde:

                return count
            else:
                cutted=len(queue[hiprio+1:])
                queue=queue[hiprio+1:]+queue[:hiprio]
                if targetinde>hiprio:
                    targetinde -= hiprio + 1
                else:
                    targetinde+=cutted
    return count

testcases=int(input())
for i in range(testcases):
    quelen, target=map(int,input().split(" "))
    queue=list(map(int,input().split(" ")))
    print(prioprint(quelen, target, queue))