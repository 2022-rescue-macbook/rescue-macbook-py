
class Queue(list):
    enQueue = list.append

    def deq(self):
        return self.pop(0)

    def get_data(self):
        return self[0]

    def Queue_size(self):
        return len(self)

T=int(input())
for x in range(0,T):
    num, find_index= list(map(int, input().split())) #int 형으로 입력받음
    arr =list(map(int, input().split()));
    q=Queue();
    for x in range(0,len(arr)):
        q.enQueue(arr[x])
    arr.sort(reverse=True) #내림차순으로 정렬
    flag=True
    count=0

    while flag:
        find=arr.pop(0)
        while 1:
           if find==q.get_data():
               if find_index==0:
                   count+=1
                   flag=False
                   break
               q.deq()
               find_index -= 1
               count+=1
               break
           else:
               temp=q.deq()
               q.enQueue(temp)
               find_index-=1
               if find_index==-1:
                   find_index=q.Queue_size()-1
    print(count)
