T = int(input())
for test in range(T):
    N, M = map(int, input().split())
    prefer = list(map(int, input().split()))

    counting = 0

    while True:
        if M == 0:
            if prefer[0] == max(prefer):
                counting += 1
                break
            else:
                prefer.append(prefer[0])
                del prefer[0]
                M = len(prefer)-1
                
        else:
            if prefer[0] == max(prefer):
                del prefer[0]
                counting += 1
                M -= 1
            else:
                prefer.append(prefer[0])
                del prefer[0]
                M -= 1
 
    print(counting)