'''
    Write a python program to scrape the list of links available in this Github repository (https://github.com/vinta/awesome-python) and search them by exact name from the console. Search result should return the github url of the result repository. 

    Expected output: 

    $ python search_repos.py
    > Query? graphene 
    > Output: https://github.com/graphql-python/graphene/

    The list should be scraped and kept in a runtime variable as soon as the program is initialized.. Handle the error with a suitable error message in case the exact name is not matched from the list. 


'''

from general import *
if __name__=="__main__":
    scrap_github()