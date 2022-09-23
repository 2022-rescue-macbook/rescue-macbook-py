t = int(input())
result = list()
for a in range(t):
    cnt = 0
    num, docu = input().split()
    num, docu = int(num), int(docu)
    input_ar = input().split()
    queue = []
    for i in input_ar:
        queue.append(int(i))
    secondlist = []
    for i in range(len(queue)):
        secondlist.append(i)
    docu_max = int(max(queue))

    if len(queue)==1:
        result.append(1)

    else :
        while len(queue)!=0 :
            docu_temp = queue.pop(0)
            secondlist_temp = secondlist.pop(0)
            if docu_temp < docu_max:
                queue.append(docu_temp)
                secondlist.append(secondlist_temp)
                continue
            cnt += 1
            if len(queue) != 0:
                docu_max = max(queue)
            if secondlist_temp == docu:
                result.append(cnt)
                break

for i in result:
    print(i)
