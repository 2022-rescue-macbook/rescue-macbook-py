times = int(input())

answer = []
for i in range(times):
    number, choice = list(map(int, input().split()))
    Queue = list(map(int, input().split()))
    count = 0
    while True:
        if Queue[0]<max(Queue):
            if choice == 0:
                choice = len(Queue) -1
            else:
                choice -=1            
            Queue.append(Queue[0])
        else:
            count +=1
            if choice == 0:
                answer.append(str(count))
                break
            else:
                choice -=1       
        del Queue[0]
        # print(choice)

print('\n'.join(answer))
exit(0)