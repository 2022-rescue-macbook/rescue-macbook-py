case = int(input())

for _ in range(case):
    N, M = map(int, input().split())
    # https://dojang.io/mod/page/view.php?id=2179
    # N, M = input().split()
    # N = int(N)
    # M = int(M)
    
    print_list = list(map(int, input().split()))
    prior_number = [] # prior number에 모든 수를 넣어 우선순위의 max 숫자 확인할 때 쓴다

    # 우선순위를 탐색하기 위한 리스트
    for doc in print_list:
        prior_number.append(doc) # 문서를 prior_number 리스트에 넣어주기
            
    # queue 안에 index를 넣어 탐색    
    result = [0 for _ in range(N)] # [(변수를 활용한 값) for (사용할 변수이름) in (순회할 수 있는 값)]
    queue = [i for i in range(N)]
    sequence = 1 # sequence로 해당 숫자가 몇 번째로 꺼내지는 지를 표시한다
    
    while queue:
        if print_list[queue[0]] == max(prior_number):
        # queue 의 첫번째 자리 숫자가 prior_number 리스트 안의 가장 높은 숫자라면
        
            prior_number.remove(max(prior_number))
            # 그 문서를 prior_number 리스트에서 제거하고
            # result 리스트안에 담아줌
            result[queue.pop(0)] = sequence
            # pop(x)는 리스트의 x번째 요소를 돌려주고 그 요소를 삭제한다
            
            sequence += 1
            # 만약 4,3,2,1 순으로 담겨져 있다면 1은 4번째로 꺼내짐
        
        else:
            queue.append(queue.pop(0))
            # 가장 높은 숫자가 아니라면 queue의 첫번째 요소를 queue의 뒷부분으로 다시 보냄
            # 앞자리에서 뒷부분으로 보냄 => 앞자리에서 제거 + 뒷자리에 추가
            
    print(result[M])