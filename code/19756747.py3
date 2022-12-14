Case = int(input())

def priority_print(queue, M, print_count):
    priority = max(queue.values())
    
    for key, item in queue.items():
        if(priority == item):
            if(M == key):
                return print_count
            else:
                queue.pop(key)
                return priority_print(queue, M, print_count + 1)
        else:
            cur_key = key
            cur_item = item
            queue.pop(cur_key)
            queue.update({cur_key: cur_item})
            return priority_print(queue, M, print_count)

for _ in range(Case):
    N, M = map(int, input().split())
    
    if(N == 1):
        dummy = input()
        print(1)
        continue
    
    num_list = map(int, input().split())
    
    queue = dict()
    for i, num in enumerate(num_list):
        queue[i] = num
        
    print(priority_print(queue, M, 1))