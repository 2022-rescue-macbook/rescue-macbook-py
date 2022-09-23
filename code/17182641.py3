number = int(input())
answer = []
NM = []
for i in range(0,number):
    NM = list(map(int,input().split()))
    number_of_card = NM[0]
    location = NM[1]
    count = 0
    priority = list(map(int, input().split()))
    while 1:
        flag = True
        for j in range(1,len(priority)):
            if priority[0] < priority[j]:
                pop = priority.pop(0)
                priority.append(pop)
                location = (location-1) % len(priority)
                flag = False
                break
        if flag:
            priority.pop(0)
            count += 1
            if location == 0:
                answer.append(count)
                break
            location = (location - 1) % len(priority)
for i in answer:
    print(i)
