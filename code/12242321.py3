tase_case = int(input())
order = []
input_data = []
priority_queue = []

for _ in range(tase_case):
    input_data.append([input() for x in range(2)])

for i in input_data:
    N, M = i[0].split()
    priority = i[1].split()
    priority = [int(x) for x in priority]
    priority_queue = [[n, x] for n, x in enumerate(priority)]

    while 1:
        if priority_queue[0][1] < max(priority):
            priority_queue = priority_queue[1:] + priority_queue[0:1]
        else:
            order.append(priority_queue[0])
            priority.remove(priority_queue[0][1])
            priority_queue.remove(priority_queue[0])
        if len(priority_queue) == 0:
            break
        
    for i in order:
        if i[0] == int(M):
            print(order.index(i) + 1)

    order = []
