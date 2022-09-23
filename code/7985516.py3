# coding=<utf-8>
class paper:
    def __init__(self,important):
        self.seq = 0
        self.important = important
    def setPaper(self,seq,important):
        self.seq =seq
        self.important =important
        
def remove_insert(list):
    temp = list.pop(0)
    list.append(temp)
    #printList(list)

def findMax(list,present):
    for i in list: 
        if(present.important < i.important ):
            return True
    return False

def printList(list):
    for i in range(0,len(list)):
        print(list[i].important)
    
    
    

testCase = input()
maxNum  =0 
list = [] 

for t in range(0,int(testCase)):
    count = 0

    while(len(list) > 0):
        list.pop()
    
    n,m= input().split()
    str = input().split()
    pointer = ""
    
    for i in str:
        p =  paper(i)
        list.append(p)
     
    pointer = list[int(m)]
    
    #print("start" , pointer.important)
    #@printList(list)
    
    while(len(list) > 0):
        present = list[0]    
        #print(" now Present " ,present.important)
        
        if ( findMax(list, present) ) : 
            remove_insert(list)
            #print("remove insert")
        else:
           # print("list pop()")
            count+=1
            if( present == pointer ):
                print(count)
                break 
            list.pop(0)            