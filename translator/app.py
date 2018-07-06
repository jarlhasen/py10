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
    w = w.lower() # all the data in the json file is in lower case.
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys())) >0: # make sure that we have a result in the list and the list not a blank list
        yn = input("Did you mean [%s] instead?  \nEnter Y if yes, or N if NO:\n" % get_close_matches(w,data.keys())[0])
        yn = yn.upper() # Just incase the user entered a 'y' instead of 'Y'
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]  # user agreede that that is the best answer.
        elif yn == "N":
            return "The word dosen't exist ,please double check it !"
        else:
            return "we didn't understand your entry."
    else:
        return "The word dosen't exist ,please double check it !"
# this is the user pace.
word = input("Enter a word:")
print(translate(word))


# remember to use python standard library

# we also have to match out the most similar words given by the user and return a most possible words by.

