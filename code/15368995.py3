import sys

case = int(input())

for _ in range(case):
    N, M = map(int, input().split())
    print_list = list(map(int, input().split()))
    priority_docs = []
    result = [0 for _ in range(N + 1)]
    queue = [i for i in range(N)]
    
    for doc in print_list:
        priority_docs.append(doc)
    
    sequence = 1
    while queue:
        if print_list[queue[0]] == max(priority_docs):
            priority_docs.remove(max(priority_docs))
            result[queue.pop(0)] = sequence
            sequence += 1
        else:
            queue.append(queue.pop(0))              
    print(result[M])