n = int(input("number: "))
mn = 2
def calc(mn,n):
    if n <= 1:
        return 'Try other number'
    else:
        if mn >= n:
            return n, 'is a prime number'
        else:
            if n==2:
                return n, 'is a prime number'
            elif n%mn == 0:
                return n, 'is NOT a prime number'
            else:
                return calc(mn+1,n)
            
    return n, 'is NOT a prime number'

print(calc(mn,n))
