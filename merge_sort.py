from random import randint

def merge_sort(items):

	if len(items) == 0:
		return []
	
	if len(items) == 1:
		return items
	
	if len(items) == 2:
		if items[0] < items[1]:
			return items
		
		return [items[1], items[0]]


	mid = len(items) // 2
	left = merge_sort(items[:mid])
	right = merge_sort(items[mid:])

	output = []
	l_index, r_index = 0, 0

	while l_index < len(left) and r_index < len(right):
		l_item = left[l_index]
		r_item = right[r_index]
		
		if l_item < r_item:
			output.append(l_item)
			l_index += 1
		else:
			output.append(r_item)
			r_index += 1

	output.extend(left[l_index:])
	output.extend(right[r_index:])

	return output

for _ in range(10000):
	numbers = [randint(-100, 100) for i in range(randint(0, 100))]
	if sorted(numbers) != merge_sort(numbers):
		print("Test failed", numbers)

