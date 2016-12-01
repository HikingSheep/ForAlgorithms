string = input("string: ")
vowels = ("a","e","i","o","u","A","E","I","O","U")

def Remove(string):
    for element in string:
        if element in vowels:
            string = string.replace(element,"")
            Remove(string)
    else:
        return string

print(Remove(string))

            
