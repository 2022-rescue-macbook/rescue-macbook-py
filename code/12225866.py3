test_m = int(input())
for i in range(test_m):
    seq = 1
    doc_num, target = input().split()
    #for j in range(int(doc_num)):
    target = int(target)
    doc_num = int(doc_num)
    line = input()
    queue = line.split()
    while(1):
        #print(target,seq)
        max_prior = max(queue)
        poped = queue.pop(0)
        if(int(poped) >= int(max_prior)):
            if(target == 0):
                print(seq)
                break
            seq += 1
        else :
            queue.append(poped)
        #print(queue)
        target -= 1
        target = target % (len(queue))
        #print(tokens)
