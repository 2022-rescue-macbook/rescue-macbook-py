import sys
#a = list(map(int, sys.stdin.readline().split()))

#a=sys.stdin.readline().strip()

# lines=sys.stdin.readlines()
#
# for line in lines:
#     k=list(map(int,line.split()))
#
#     print(k[1]//(k[0]+1))

a=int(sys.stdin.readline().strip())
first=[]
second=[]
for _ in range(a):
    first.append(list(map(int, sys.stdin.readline().split())))
    second.append(list(map(int, sys.stdin.readline().split())))

for i in range(a):
    find_index=first[i][1]
    checker=False
    number=0
    while(checker==False):
        if(max(second[i])==second[i][0]):
            second[i].pop(0)
            number+=1
            if(find_index==0):
                checker=True
                print(number)
            else:
                find_index-=1
        else:
            second[i].append(second[i].pop(0))
            if(find_index==0):
                find_index=len(second[i])-1
            else:
                find_index-=1

