t = int(input())
testcase = [list(map(int, input().split())) for _ in range(t*2)]

def printer(test, papers):
    index = test[1]
    printed = 0
    print_index = False
    while print_index == False:
        if papers[0] < max(papers):
            if index == 0:
                index = len(papers)-1
            else:
                index -= 1
            papers.append(papers.pop(0))
        else:
            if index == 0:
                print_index = True
            papers.pop(0)
            index -= 1
            printed += 1
    
    return printed

for i in range(t):
    print(printer(testcase[i*2], testcase[i*2+1]))