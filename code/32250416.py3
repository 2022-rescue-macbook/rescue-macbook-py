import sys

T = int(sys.stdin.readline())
for _ in range(T):
    printer = []
    p_dict={}
    order = 1
    N,M = map(int,sys.stdin.readline().split())
    printer = list(map(int,sys.stdin.readline().split()))
    for i in printer:
        if p_dict.get(i) is None:
            p_dict[i] = 1
        else:
            p_dict[i] +=1
    while True:
        if M == 0:
            if max(p_dict)==printer[0]:
                sys.stdout.write(str(order)+'\n')
                break
            else:
                printer.append(printer[0])
                del printer[0]
                M = len(printer)-1
        else:
            if max(p_dict)==printer[0]:
                if p_dict[printer[0]] ==1:
                    del p_dict[printer[0]]
                else:
                    p_dict[printer[0]] -=1
                del printer[0]
                order+=1
                M -=1
            else:
                M -=1
                printer.append(printer[0])
                del printer[0]