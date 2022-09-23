from operator import itemgetter


def q_finder(numbers, target_position, order):
	first = numbers[0]


	for i in range(1, len(numbers)):
		if(numbers[i][0] > first[0]):
			numbers.append(first)
			numbers.pop(0)

			return q_finder(numbers, target_position, order)

	if(first[1]== target_position):
		return order

	return q_finder(numbers[1:], target_position, order+1)


n = int(input())
for i in range(n):
	number, m= [int(x) for x in input().split()]
	numbers = []
	target_position = m

	numbers = [int(x) for x in input().split()]
	number_pair = [(numbers[y],y) for y in range(len(numbers)) ]
	
	print(q_finder(number_pair, target_position, 1))