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


#PERFECT_SQUARE(P)
        #integral <- 0
        #if(P is greater or equal 0) 
            #while integral * integral < P
                #integral <- integral + 1
            #if(integral * integral != P)
                #x <- sqrt(P)
                #x <- floor(x**2)
                #return (output( x is the highest square, input: P))
            #else
                #return (output( P  is a perfect square integral))
        #else
            #output(P is not a positive integral)
