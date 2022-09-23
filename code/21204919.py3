import sys
def solution(priorities, location):
    answer = 0
    queue = []
    sorted_queue = []
    for i in range(len(priorities)):
        queue.append((priorities[i],i))
    while len(queue) != 0:
        count = 0
        for i in range(len(queue)):
            if queue[0][0] < queue[i][0]:
                k = queue[0]
                del queue[0]
                queue.append(k)
                count += 1
        if count == 0 :
            sorted_queue.append(queue[0])
            del queue[0]
    for i in range(len(sorted_queue)):
        if sorted_queue[i][1] == location:
            answer = i + 1
    return answer

iter = int(sys.stdin.readline())
for k in range(iter):
    temp = sys.stdin.readline().replace("\n","").split()
    user_input = sys.stdin.readline().replace("\n","").split()
    user_input = list(map(lambda x : int(x), user_input))
    print(solution(user_input,int(temp[1])))