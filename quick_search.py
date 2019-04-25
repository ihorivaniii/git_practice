from random import randrange


def binary_search(sorted_list, target):
    if not sorted_list:
        return 'value not found'
    mid_idx = len(sorted_list) // 2
    mid_val = sorted_list[mid_idx]
    if mid_val == target:
        return mid_idx
    if mid_val > target:
        left_half = sorted_list[:mid_idx]
        return binary_search(left_half, target)
    if mid_val < target:
        right_half = sorted_list[mid_idx + 1:]
        result = binary_search(right_half, target)
        if result is 'value not found':
            return result
        return result + mid_idx + 1


def quicksort(list, start, end):
    if start >= end:
        return
    pivot_idx = randrange(start, end + 1)
    pivot_element = list[pivot_idx]

    list[end], list[pivot_idx] = list[pivot_idx], list[end]

    less_than_pointer = start

    for i in range(start, end):
        if list[i] < pivot_element:
            list[i], list[less_than_pointer] = list[less_than_pointer], list[i]

            less_than_pointer += 1

    list[end], list[less_than_pointer] = list[less_than_pointer], list[end]
    quicksort(list, start, less_than_pointer)
    quicksort(list, less_than_pointer + 1, end)


list = [randrange(100) for i in range(1001)]
list_for_sort = list[:]
sorted_values = quicksort(list_for_sort, 0, 1000)
print(binary_search(list_for_sort, 16))