import json

import difflib 
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return(data[w])
    elif w.title() in data:
        return(data[w.title()])
    elif len(get_close_matches(w, data.keys())) > 0:
        answer = input("Did you mean %s instead? (y or n) " % get_close_matches(w, data.keys())[0])
        if answer == 'y':
            return(translate(get_close_matches(w, data.keys())[0]))
        elif answer == 'n':
            return("Please try again. The word doesn't exist.\n")
        else:
            #if the user enters neither Y nor N
            return("We didn't understand your entry.\n")
    else:
        return("Please try again. The word doesnt exist.")


word = input("Enter a word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
    print("\n")
else:
    print(output)

