import random

def calc(array):
    a = len(array)
    for elements in range(a-1,0,-1):
        e = random.randint(0,elements)
        array[elements],array[e] = array[e],array[elements]
    return array
