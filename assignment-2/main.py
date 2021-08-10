'''
    Write a python class that is able to return the meaning of an English language word provided to it in the terminal. (Use https://dictionaryapi.dev/) 

    Expected output:
    $ python dictionary_search.py
    > Word? <user inputs the word “House”>
    > Output: House. Noun. A building for human habitation, especially one that is lived in by a family or small group of people.  


'''

from general import *

if __name__=="__main__":
    query = input("Query? ")
    if query:
        dictionary = DictionarySearch(query)
        # get the meaning of the word
        meaning = dictionary.get_meaning()
        if meaning:
            print("Output: ",meaning)
        else:
            print("Could not match word you are searching for. Please try again.")
    else:
        print("Please try again.")
    