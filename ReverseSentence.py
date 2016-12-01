def reverse(sentence):
    listy = []
    answer = ""
    words = sentence.split()
    for word in words:
        listy.insert(-1,word)
    return answer.join(listy)

sentence = input("Input: ")
print(reverse(sentence))
