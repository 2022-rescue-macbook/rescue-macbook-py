caseNum = int(input())
for x in range(caseNum):
    n, m = map(int, input().split(" "))
    arr = list(map(int, input().split(" ")))
    
    enumArr = list(enumerate(arr))
    target = enumArr[m]
    arr.sort(reverse=True)

    index = 0
    count = 0
    while True:
        if enumArr[index][1] == arr[0]:
            count += 1
            if enumArr[index] == target:
                print(count)
                break
            arr.pop(0)
            enumArr.pop(index)
            index -= 1
        if (index == len(enumArr) - 1):
            index = 0
        else:
            index += 1