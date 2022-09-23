class printerqueue :
    case = int(input())

    i = 0
    while i < case :
        count = 0;
        inst = input().split()
        cnt = int(inst[0])
        pos = int(inst[1])
        priority = input().split()

        while 1 :
            comp = 0
            for pri in priority :
                if priority[0] < pri :
                    comp = 1
                    break
            if comp :
                tmp = priority.pop(0)
                priority.append(tmp)
                if pos == 0 :
                    pos = len(priority) - 1
                else :
                    pos -= 1
            else :
                priority.pop(0)
                count += 1
                if pos == 0 :
                    print(count)
                    break
                else :
                    pos -= 1
        i += 1
