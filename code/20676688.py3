T = int(input())

for i in range(T):
    count = 0
    final_list = []
    final_index = []
    N, M =map(int,input().split(' '))
    initial_index =[i for i in range(N)]
    initial_list = list(map(int,input().split(' ')))
    while initial_list != [] and M not in final_index:
        if initial_list[0] == max(initial_list):
            final_list.append(initial_list.pop(0))
            final_index.append(initial_index.pop(0))
            count+=1
        else :
            initial_list.append(initial_list.pop(0))
            initial_index.append(initial_index.pop(0))
  
    print(count)
