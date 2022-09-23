testcase = int(input())
answer = []

for i in range(testcase):
    N,M = list(map(int,input().split(' ')))
    num = list(map(int,input().split(' ')))
    num_index = [i for i in range(len(num))]

    count = 1
    while(M in num_index):
        max_num = max(num)
        if (max_num == num[0]):
            if(num_index[0] == M):
                answer.append(count)
            del num[0]
            del num_index[0]
            count= count+1
        else:
            num.append(num[0])
            num_index.append(num_index[0])
            del num[0]
            del num_index[0]
for i in answer:
    print(i)