def calc(num):
    mn = 1                          #1
    answer = 0                      #1
    while num >= mn:                #n
        mn = mn*5                   #n
        answer = answer + num//mn   #n
    return answer                   #1

#1 + 1 + n + n + n + 1
#3 +3n /3
#1 + n
#O(n)
