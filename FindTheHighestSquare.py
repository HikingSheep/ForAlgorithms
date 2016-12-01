import math
def calc(p):
    inty = 0
    if p >= 0:
        while inty * inty < p:
            inty += 1
        if inty*inty != p:
            x = math.sqrt(p)
            x = math.floor(int(x)**2)
            return(print(x,'is the highest square, input:',p))       
        else:
            return(print(p,'is a perfect square of',inty))

    else:
        print(p,'is not a positive integral')
