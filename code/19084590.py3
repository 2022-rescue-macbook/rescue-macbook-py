def solution():
    result = []
    
    for case in range(int(input())):
        num, idx = list(map(int, input().split()))
        queue = list(map(int, input().split()))
        
        print_num = 0
        while queue:
            if queue[0] == max(queue):
                queue.pop(0)
                print_num += 1
                num -= 1
                if idx == 0:
                    break
            else:
                curr = queue.pop(0)
                queue.append(curr)
            idx = (idx - 1) % num
        
        result.append(print_num)
        
    for r in result:
        print(r)
        
solution()