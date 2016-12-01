def seq(n):
    
    curArray = []
    maxSub = []

    curArray = [n[0]]

    for i in range (1, len(n)):
        curr = n[i]
        prev = n[i-1]
        if curr > prev:
            curArray.append(curr)
        elif len(curArray) > len(maxSub):
            maxSub = curArray
            curArray = [curr]
        else:
            curArray = [curr]

    if len(maxSub) < len(curArray):
        return curArray
    
    return maxSub

n = [1,2,3,4,1,5,1,6,7]
print(seq(n))
