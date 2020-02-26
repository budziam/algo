from random import randint

def quick_sort(items):
	if len(items) == 0:
		return []

	mid = len(items) // 2
	mid_item = items[mid]

	less = [i for i in items if i < mid_item]
	exact = [i for i in items if i == mid_item]
	more = [i for i in items if i > mid_item]

	return quick_sort(less) + exact + quick_sort(more)

for _ in range(10000):
	numbers = [randint(-100, 100) for i in range(randint(0, 100))]
	if sorted(numbers) != quick_sort(numbers):
		print("Test failed", numbers)
		break

