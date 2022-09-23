#algorithm
def function(LnD,Queue): # Length of list and Document = LnD
    count = 0
    check_list = [0] * LnD[0]
    check_list[LnD[1]] = 1
    while True:
        if max(Queue) == Queue[0]:
            if check_list[0] == 1:
                count += 1
                return count
            del Queue[0]
            del check_list[0]
            count += 1
        else:
            goToBack = Queue[0]
            Queue.append(goToBack)
            del Queue[0]
            goToBack = check_list[0]
            check_list.append(goToBack)
            del check_list[0]

#main
T = int(input())
for _ in range(T):
    LnD = list(map(int,input().split()))
    Queue = list(map(int,input().split()))
    print(function(LnD,Queue))