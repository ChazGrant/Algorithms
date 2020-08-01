def quickSort(arr):
    if len(arr) < 2:
        return arr
    else:
        mid = arr[0]

        less = [i for i in arr[1:] if i <= mid]
        higher = [i for i in arr[1:] if i > mid]

        return quickSort(less) + [mid] + quickSort(higher)


if __name__ == "__main__":
    l = [5, 6, 9, 1, 3, 7, 23]
    print(quickSort(l))
