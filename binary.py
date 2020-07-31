def bn(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = int((low + high) / 2)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1 
        else:
            low = mid + 1
    return None

l = [1, 5, 7, 9, 13, 15]
print("Exist") if bn(l,6) else print("Not exist")