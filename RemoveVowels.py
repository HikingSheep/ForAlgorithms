string = input("string: ") # type string
vowels = ("a","e","i","o","u","A","E","I","O","U") #tuple of vowels

def Remove(string):
    for element in string: # start loop, checking  letters in string
        if element in vowels: # check if letter is in vowels
            string = string.replace(element,"") # replace first occurance
            Remove(string) # repete unitl no occurances
    else:
        return string # return string without vowels

print(Remove(string)) # inicialize function

            
