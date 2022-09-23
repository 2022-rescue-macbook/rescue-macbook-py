import sys

def checkPriority(arData:list): # Function Annotation
    # 파이썬의 고질적인 return or parameter 타입 표기의 문제를 완화시켜주는 애
    # arData:list의 뜻은 arData라는 변수가 parameter로 들어오는데, 얘는 list여야한다는뜻
    maxNum = 9 # 가장 높은 우선순위부터 깎으면서 순위를 넣어줄 예정
    breakPoint = len(arData) # 데이터의 크기를 잼
    # count랑 index를 사용할건데, 방금 보여준것과 같이 index로 데이터를 조회했을때, 값이 존재하지 않으면 error가 남
    # error type은 ValueError로 try except구문을 쓰거나 count로 있나 없나 조회를 해보고 index해도 됨.
    # 후자를 추천함. try except는 구멍난 배에 테이프로 막는것과 비슷해서 남발하면 침몰함
    result = list() # 우선순위대로 이 리스트에 한꺼번에 저장한 후 결과를 뽑을예정
    for i in range(10):
        if arData.count(maxNum) > 0:
            tryIndex = arData.index(maxNum) # 현재 인덱스는 처음 딱 한번만 선언해주는데, 가장 앞에 있으면서 가장 큰 우선순위를 가진 인덱스가
                                            # 무조건 첫번째이고 이후부턴 따로 선언 X
            break
        else:
            maxNum-=1
    nextTarget = 0
    while True:
        if breakPoint == arData.count(0): # 7번줄에서 선언한걸 가지고와서 0인 숫자가 리스트의 크기와 같으면 리턴하고 종료
            # 같다는건 즉 모든 값이 0으로 되어있다는 뜻이라서
            return result # 리턴 값을 토대로 m번째 값이 몇번 인덱스에 있는지 찾음. 그게 곧 그 값의 출력 순서
        if arData.count(maxNum) == 0:
            maxNum -= 1
        for i in range(arData.count(maxNum)):
            try:
                nextTarget = arData.index(maxNum,tryIndex)
            except ValueError:
                nextTarget = arData.index(maxNum)
            tryIndex = nextTarget
            if tryIndex >= len(arData):
                tryIndex = 0
            if arData[tryIndex] == maxNum:
                result.append(tryIndex)
                arData[tryIndex] = 0
            tryIndex += 1

def main():
    nInputTestCase = int(sys.stdin.readline())
    # 문서의 개수n, 조회할 데이터 순서 m :: 예) 4개의 문서 중 0번째 데이터의 출력순서가 궁금하다
    # 사족을 붙이자면, 프로그래밍은 나비효과 정도로 생각해야함.
    # 첫번째 분기에서 어떤 코드를 짜느냐에 따라 프로그래밍 방식이 달라짐.
    # 다만, 정답이 정해지지 않은건 같음 모든게 정답이자 정답이 아님.
    # 여기서 n,m이라 정의했지만, 어차피 2개의 데이터가 고정적으로 들어오고 n,m쓰기 귀찮아서 리스트로 관리할 생각
    for i in range(nInputTestCase):
        queueList = list(map(int,sys.stdin.readline().split())) # 6 0
        # prioirties
        priorities = list(map(int,sys.stdin.readline().split())) # 1 1 9 1 1 1

        # 여기서도 하나의 분기가 생길수도 있을듯.
        # 6 0 / 1 1 9 1 1 1 의 예제를 볼때, 6개의 문서 중 0번인덱스가 몇번째로 출력되는지를 알고싶은건데, 
        # 우선순위를 for문을 이용해 n개의 데이터의 우선순위를 받느냐, 아니면 상관없이 그냥 받느냐의 차이
        # 참고로 해당 문제는 상관이 없지만, 실제 코딩의 경우 전자로 짜야함

        priorList = checkPriority(priorities) # 실질적인 계산하는 함수. 우선순위가 높은대로 리스트에 꽂아줌

        result = priorList.index(queueList[1]) + 1
        print(result)
        
        

main()