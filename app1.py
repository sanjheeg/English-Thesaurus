import json

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return(data[w])
    elif len(get_close_matches(w, data.keys())) > 0:
        answer = input("Did you mean %s instead? (y or n) " % get_close_matches(w, data.keys())[0])
        if answer == 'y':
            return(translate(get_close_matches(w, data.keys())[0]))
    else:
        return("Please try again. The word doesnt exist.")


word = input("Enter a word: ")

print(translate(word))

