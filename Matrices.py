addit = [[0,0],[0,0]]
Mull = [[0,0],[0,0]]
Sub = [[0,0],[0,0]]
b = [[1,2],[3,4]]
c = [[5,6],[7,8]]

def add(b,c):
    for i in range(len(b)):                 #n
       for j in range(len(c[0])):           #n^2
           addit[i][j] = b[i][j] + c[i][j]  #n^2

    for r in addit:                         #n
       print(r)                             #1

#1 + 2n + 2n^2
#O(n^2)
    
def mult(b,c):
    for i in range(len(b)):                     #n
       for j in range(len(c[0])):               #n^2
           for k in range(len(c)):              #n^4
               Mull[i][j] += b[i][k] *  c[k][j] #n^4

    for r in Mull:                              #n
       print(r)                                 #1

#1 + 2n + n^2 + n^4
#0(n^4)

def substr(b,c):
    for i in range(len(b)):
       for j in range(len(c[0])):
           Sub[i][j] = b[i][j] - c[i][j]

    for r in Sub:
       print(r)
#O(n^2)

print('Addition',add(b,c))
print('Multiplication',mult(b,c))
print('2xAddition',add(addit,addit))
print('Substraction',substr(Mull,addit))
#a = substr(mult(b,c)-(add(b,c)+add(b,c)))
#a = substr(mult - (2add))
