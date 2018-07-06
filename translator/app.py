import json

from difflib import get_close_matches #we have to consider that user may enter a wrong word, for example user may enter a rainn instead of rain.

data = json.load(open("data.json"))

# def translate(w):
#     w = w.lower() #Every word there is a lover case letters in the data file ,so we can turn every letter to a lower case letters first.
#     if w in data:
#         return data[w]
#     else:
#         return "The word dosen't exist ,please double check it !"

# version two : we make the program alittle bit smarter let's make really interesting

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys())) >0:
        return "Did you mean %s instead?" % get_close_matches(w,data.keys())[0]
word = input("Enter a word:")
print(translate(word))


# remember to use python standard library

# we also have to match out the most similar words given by the user and return a most possible words by.

