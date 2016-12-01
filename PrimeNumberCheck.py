n = int(input("number: "))
a = 2
def calc(a,n):
    if n <= 1:
        return 'Try other number'
    else:
        if a >= n:
            return n, 'is a prime number'
        else:
            if n==2:
                return n, 'is a prime number'
            elif n%a == 0:
                return n, 'is NOT a prime number'
            else:
                return calc(a+1,n)
            
    return n, 'is NOT a prime number'

print(calc(a,n))

#PRIME_NUMBER(a,n):
        #if n < 1 or n <- 1:
            #output Try other numbers
        #else:
            #if a > n or a <- n:
                #output n is a prime number
            #else:
                #if n = 2:
                    #output n is a prime number
                #else if n % a = 0:
                    #output n is not a prime number
                #else:
                    #output PRIME_NUMBER(a+1,n)
        #output n is not a prime number
