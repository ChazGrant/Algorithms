def sum(arr):
    '''
    Various realization
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 0:
        return 0
    '''
    if arr == []:
        return 0
    else:
        return arr.pop() + sum(arr)

if __name__ == "__main__"
    l = [1,5,6,7]
    print(sum(l))