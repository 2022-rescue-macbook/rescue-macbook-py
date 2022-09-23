number_of_testcases=int(input())
answer_list=[]
def organize(importance,location):
    answer=0
    while True:
        if importance[0]==max(importance):
            answer=answer+1
            if location==0:
                return answer
                break
            else:
                importance.remove(importance[0])
                location=location-1
        else:
            importance.append(importance[0])
            importance.remove(importance[0])
            if location==0:
                location=len(importance)-1
            else:
                location=location-1
for k in range(0,number_of_testcases):
    location=int(input().split(" ")[1])
    importance=input().split(" ")
    answer_list.append(organize(importance,location))
for k in answer_list:
    print(k)