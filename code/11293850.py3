T = int(input())

li_queue = []

for t in range(T):
    N, M = map(int, input().split())
    msg = input().split()

    li_queue.clear()
    cnt = 1
    
    for m in msg:
        li_queue.append(int(m))

    idx = 0
    max_value = max(li_queue)
    max_idx = li_queue.index(max_value)

    while(True):
        if idx==len(li_queue):
            idx = 0

        if li_queue[idx] != max_value:
            idx = max_idx
            li_queue[idx] = -1

            max_value = 0
            max_idx = 0

            for temp_idx, temp_value in enumerate(li_queue[idx:]):
                if temp_value>max_value:
                    max_value = temp_value
                    max_idx = temp_idx + idx

            if max_value < max(li_queue):
                max_value = max(li_queue)
                max_idx = max_idx = li_queue.index(max_value)

            if M == idx:
                print(cnt)
                break
            idx+=1
            cnt+=1

        else:
            if M == idx:
                print(cnt)
                break
            else:
                li_queue[idx] = -1
                cnt+=1
                
                max_value = 0
                max_idx = 0

                for temp_idx, temp_value in enumerate(li_queue[idx:]):
                    if temp_value>max_value:
                        max_value = temp_value
                        max_idx = temp_idx + idx

                if max_value < max(li_queue):
                    max_value = max(li_queue)
                    max_idx = max_idx = li_queue.index(max_value)

                idx+=1