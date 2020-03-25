def heapify(a):
    for i in range(len(a) // 2 - 1, -1, -1):
        root_index = i

        while root_index < len(a) // 2:
            root = a[root_index]

            child_index = 2 * root_index + 1
            if child_index + 1 < len(a) and a[child_index + 1] > a[child_index]:
                child_index += 1

            if a[child_index] > root:
                a[root_index], a[child_index] = a[child_index], a[root_index]
                root_index = child_index


array = [1, 5, 6, 6, 8, 12, 14, 16]
heapify(array)
print(array)
