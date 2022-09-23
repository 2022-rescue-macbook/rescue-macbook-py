for i in range(int(input())):
    check = True
    num = int(input().split()[1])
    priority = [0] * 9
    print_queue = []
    result = 1
    for i,j in enumerate(map(int,input().split())):
        priority[j-1] += 1
        print_queue.append((j,i))
    while(check):
        if (sum(priority[print_queue[0][0]:]) > 0 ):
            print_queue.append(print_queue.pop(0))
        else:
            if (print_queue[0][1] == num):
                check = False
            else:
                priority[print_queue[0][0] - 1] -= 1
                print_queue.pop(0)
                result += 1
        #print(print_queue,priority,result)
    print(result)
        
        