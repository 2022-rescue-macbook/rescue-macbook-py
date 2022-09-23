import sys

for i in range(int(sys.stdin.readline().rstrip())):

    n, index = map(int, sys.stdin.readline().rstrip().split(' '))
    n_list = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    f = 0
    
    while True:
            
        if n_list[0] < max(n_list):
            n_list.append(n_list[0])
                
            if index == 0:
                index = n
        else:
            n -= 1
            f += 1

            if index == 0:
                break
            
        del n_list[0]
        index -= 1
        
    print(f)  