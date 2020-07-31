def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def sortArray(arr):
    newArray = []
    for i in range(len(arr)):
        item = findSmallest(arr)
        newArray.append(arr.pop(item))
    return newArray

l = [5,9,2,14,6,8,54]
sortl = sortArray(l)
print(sortl)