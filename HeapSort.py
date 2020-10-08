def max_heapify(heap, heap_size, root):
    left = 2 * root + 1
    right = 2 * root + 2
    larger = root
    if left < heap_size and heap[larger] < heap[left]:
        larger = left
    if right < heap_size and heap[larger] < heap[right]:
        larger = right

    if larger != root:
        heap[larger], heap[root] = heap[root], heap[larger]
        max_heapify(heap, heap_size, larger)


def build(heap, heap_size):
    for i in range(heap_size - 2 // 2, -1, -1):
        max_heapify(heap, heap_size, i)


def heap_sort(heap, heap_size):
    build(heap, heap_size)
    for i in range(heap_size-1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        max_heapify(heap, i, 0)


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    heap_sort(arr, len(arr))
    print(arr)
