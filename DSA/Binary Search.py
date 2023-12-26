def binarySearch(n, low, high, target):
    if high >= low:
        mid = (low + high) // 2
        if (n[mid] == target):
            return mid
        elif (n[mid] > target):
            return binarySearch(n, low, mid - 1, target)
        else:
            return binarySearch(n, mid + 1, high, target)
    else:
        return -1

n = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(n)    
target = int(input("Enter a target element to search: "))
result = binarySearch(n, 0, len(n)-1, target)
if result != -1:
    print(result + 1)
else:
    print('Element not found')
