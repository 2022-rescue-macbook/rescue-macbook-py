
def solution():
    TC = int(input())
    for iter in range(TC):
        N, M = map(int,(input().split()))
        input_list = list(map(int,input().split()))
        queue = []
        for index in range(len(input_list)):
            queue.append((index,input_list[index]))
        max_index, max_num = max(queue, key = lambda x : x[1])
        count = 0
        while True:
            if queue[0][0] == max_index and queue[0][1] == max_num:
                count +=1
                if queue[0][0] == M:
                    break
                queue.pop(0)
                max_index, max_num = max(queue, key = lambda x : x[1])
            else:
                index , num = queue.pop(0)
                queue.append((index,num))
        
        print(count)

solution()