import json

data = json.load(open("data.json"))

def translate(w):
    if w in data:
        return(data[w])
    else:
        return("Please try again. The word doesnt exist.")


word = input("Enter a word: ")

print(translate(word))

