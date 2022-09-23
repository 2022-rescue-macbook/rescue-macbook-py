import sys

class queue:
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return -1
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def isEmpty(self):
        if self.items:
            return 0
        return 1

    def front(self):
        if self.isEmpty():
            return -1
        return self.items[0]

    def back(self):
        if self.isEmpty():
            return -1
        return self.items[self.size() - 1]

    def print(self):
        for i in range(0, self.size()):
            print(self.items[i])

    def max(self):
        return max(self.items)
    

if __name__ == "__main__":
    testCase = int(sys.stdin.readline())
    for i in range(0, testCase):
        numQue = queue()
        checkQue = queue()
        InputData = sys.stdin.readline().split()
        N = int(InputData[0])
        M = int(InputData[1])
        InputData = sys.stdin.readline().split()
        for j in range(0, N):
            numQue.push(InputData[j])
            if j == M:
                checkQue.push(1)
            else:
                checkQue.push(0)

        count = 0

        # 반복
        while(1):
        # 최고 중요도 선정
            maxImportance = numQue.max()

            # 최고 중요도 나올때까지 que를 빼고 넣기
            while(1):
                temp = numQue.pop()
                check = checkQue.pop()
                # 나올경우 count +1
                # 맞을 경우 종료, 아니면 반복
                if maxImportance == temp:
                    count += 1
                    break
                else:
                    numQue.push(temp)
                    checkQue.push(check)
            # M에 해당하는지 확인
            if check == 1:
                break

        print(count)