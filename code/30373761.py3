import sys

n = int(input())

for _ in range(n):
    length, idx = map(int, input().split())
    temp_list = list(map(int, input().split()))
    wanted_max = temp_list[idx]
    #print(temp_list, length, idx)

    answer = 0
    while(1):
        current_max = max(temp_list)
        while(current_max != temp_list[0]):
            temp_list = temp_list[1:] + [temp_list[0]]
            if idx == 0: idx = len(temp_list) - 1
            else: idx -= 1
        if((max(temp_list) == wanted_max) and (idx == 0)):
           break;
        temp_list = temp_list[1:]; answer+= 1; idx -= 1
     #   print(temp_list, answer, idx)
    print(answer + 1)