
def reverse(sentence):
    listy = []
    answer = " "
    words = sentence.split()
    for word in words:
        listy.insert(-1,word)
    return answer.join(listy)

sentence = input("Input: ")
print(reverse(sentence))

#REVERSE-SENTENCE(sentence):
    #empty_list <- []                       1
    #empty_string <- " "                    1
    #words <- sentence split()              n
    #for word in words:                     n
        #empty_list insert (-1, word)       n
    #output empty_string join(empty_list)   n

    #1 + 1 + n + n + n + n
    #2+4n /2
    #1 + 2n
    #O(n)
