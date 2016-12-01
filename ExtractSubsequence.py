def seq(n):
    
    subseq = []
    array = [n[0]]
    
    for i in range (1, len(n)):
        curr = n[i]
        prev = n[i-1]
        if curr > prev:
            array.append(curr)
        elif len(array) > len(subseq):
            subseq = array
            array = [curr]
        else:
            array = [curr]

    if len(subseq) < len(array):
        return array
    
    return subseq

n = [1,2,3,4,1,5,1,6,7]
print(seq(n))
