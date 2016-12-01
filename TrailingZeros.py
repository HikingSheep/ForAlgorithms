def calc(num):
    mn = 1                          
    answer = 0                      
    while num >= mn:                
        mn = mn*5                   
        answer = answer + num//mn   
    return answer                   
