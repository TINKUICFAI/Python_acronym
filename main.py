words= input("Enter Words: ")

def acronym(words):
    words=words.split()
    string = ""
    for word in words:
        if word!="and" :
            string+=str(word[0])
    return string.upper()

result=acronym(words)
print(result)