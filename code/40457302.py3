# https://www.acmicpc.net/problem/1966

# 큐를 이용하여 풀어야한다.
# 조심해야할 부분은 우선순위가 낮은데 앞서 있는 경우 가장 뒤로 밀려나야한다.

def main():

    testCaseNum = int(input())
    for _ in range(testCaseNum):
        pageCnt, targetPageIndex = map(int, input().split())
        pageList = list(map(int, input().split()))

        pageList = [i * 10 for i in pageList]
        sortedPageList = sorted(pageList, reverse=True)
        pageList[targetPageIndex] += 1

        cnt = 0
        while True:
            if pageList[0] == sortedPageList[0] or (pageList[0] - 1) == sortedPageList[0]:
                if pageList[0] % 10 == 1:
                    cnt += 1
                    break
                pageList.pop(0)
                sortedPageList.pop(0)
                cnt += 1
            else:
                pageList.append(pageList.pop(0))

        print(cnt)


if __name__ == '__main__':
    main()
