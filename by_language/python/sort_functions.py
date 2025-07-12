from typing import List

def bubble_sort(list: List):
    unsorted_until_index = len(list) - 1
    sorted = False
    steps = 0

    while not sorted:
        sorted = True
        for i in range(unsorted_until_index):
            if list[i] > list[i+1]:
                sorted = False
                list[i], list[i+1] = list[i+1],list[i]
        unsorted_until_index = unsorted_until_index - 1
        steps += 1
    return list


def selection_sort(array):
    for i in range(len(array)):
        lowest_number_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[lowest_number_index]:
                lowest_number_index = j
        if lowest_number_index != i:
            array[i], array[lowest_number_index] = array[lowest_number_index], array[i]  # Swap
    return array


def insertion_sort(array: List):
    for index in range(1, len(array)):
        position = index
        temp_value = array[index]

        while position > 0 and array[position - 1] > temp_value:
            array[position] = array[position - 1]
            position = position - 1

        array[position] = temp_value

def binary_search(arr, target, left, right):
    if left > right:
        return -1

    print(arr[left:right])

    mid = int((left + right) / 2)

    print(f"Mid -> {mid}")

    if arr[mid] == target:
        return mid
    if arr[mid] > target:
        return binary_search(arr, target, left, mid-1)
    else:
        return binary_search(arr, target,mid+1, right)


list = [65, 55,45,35,25,15,10,5]

bb_sort = bubble_sort(list)

print(bb_sort)
print(binary_search(bb_sort, 15, 0, len(list)-1))

