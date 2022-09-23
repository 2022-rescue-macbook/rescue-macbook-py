

# 리스트를 랑 위치를 넣으면 숫자가 나옴
def func(list, position):
    count = 0

    while True:
        # 원하는 값 보다 큰 우선순위가 있으면 뒤로 넣어둠
        if list[0] < max(list):
            list.append(list.pop(0))
            if position == 0:
                position = len(list) - 1
            else:
                position -= 1
        # 작거나 같으면 뽑음 , 만일 뽑은게 내가 원하는 값이면 while문 종료
        else:
            list.pop(0)
            count += 1
            if position == 0:
                break
            else:
                position -= 1

    return count

#입력
import sys
input = sys.stdin.readline

n = int(input()) #테스트 케이스
answer=[] #답을 담아둘 배열

for i in range(n):
    x,y = map(int,input().split())
    temp = list(map(int,input().split())) # x만큼의 길이의 배열 만듬
    answer.append(func(temp,y))



for i in answer:
    print(i)