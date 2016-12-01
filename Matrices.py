addit = [[0,0],[0,0]]
Mull = [[0,0],[0,0]]
Sub = [[0,0],[0,0]]
b = [[1,2],[3,4]]
c = [[5,6],[7,8]]

def add(b,c):
    for i in range(len(b)):                 
       for j in range(len(c[0])):           
           addit[i][j] = b[i][j] + c[i][j]  

    for r in addit:                         
       print(r)                             
    
def mult(b,c):
    for i in range(len(b)):                     
       for j in range(len(c[0])):               
           for k in range(len(c)):              
               Mull[i][j] += b[i][k] *  c[k][j] 

    for r in Mull:                              
       print(r)                                 

def substr(b,c):
    for i in range(len(b)):
       for j in range(len(c[0])):
           Sub[i][j] = b[i][j] - c[i][j]

    for r in Sub:
       print(r)

print('Addition',add(b,c))
print('Multiplication',mult(b,c))
print('2xAddition',add(addit,addit))
print('Substraction',substr(Mull,addit))
