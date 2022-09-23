import sys
input = sys.stdin.readline
# 몇번 돌릴지
forCnt =int(input())

for i in range(forCnt):
	N ,M = map(int, input().split());
	A = list(map(int, input().split()))
    # B 리스트는 현재 A 리스트 M 번째의 위치를 표시
	B = [0] * N
    # 현재 M 위치는 1로 표시
	B[M] = 1;
    # 정답이 될 count
	count = 0;
	while(True):
        # 현재 A 리스트의 우선순위 최댓값과 현재 A 리스트 맨 앞 우선순위 값을 비교
		if A[0] == max(A):
            # 현재 A 리스트 맨 앞 값이 우선 순위가 제일 높은면 A를 pop
			A.pop(0);
            # 방금 뽑은게 우리가 뽑아야할 친구면 break 
			if(1 == B.pop(0)):
				break;
            # 아니면 
			count += 1;
		else:
            # 현재 A 리스트 맨 앞 값이 우선 순위가 제일 높지 않으면 A,B 리스트의 맨 앞 값을 맨 뒤로 ㅇㅇ
			A.append(A.pop(0))
			B.append(B.pop(0))
	print(count+1)