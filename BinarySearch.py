array = [2,3,5,7,9,13]
def binary_search(array,low,high):
    lower = 0
    upper = len(array)
    while lower < high:
        x = lower + (upper - lower) // 2
        val = array[x]
        target = high - 1
        if low <= target == val and target <= high:
            return True
        elif target > val:
            if lower == x:   
                break       
            lower = x
        elif target < val:
            upper = x
    return False

low = int(input("Low: "))
high = int(input("High: "))
print(array)
print(binary_search(array,low,high))
