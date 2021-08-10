from bs4 import BeautifulSoup
from config import *
import requests

def get_query_string():
    ''' 
        take query string from user to search 
    '''
    search_str = input("Query? ")
    return search_str

def search_again(all_links):
    '''
        ask user to search for another link
    '''
    search = input("Search again?(Y/N) ")
    if search.lower()=="y":
        query_str = get_query_string()
        search_query_str(all_links,query_str)
    elif search.lower()=="n":
        return
    else:
        print("Unknown input. Try again.")

def search_query_str(all_links,str):
    '''
        return link(s) if query string present in link
    '''
    flag = False
    for each_link in all_links:
        if str in each_link:
            print("Output: ", each_link)
            flag = True
    if not flag:
        print("Could not find any link. Please try again.") 
    search_again(all_links)

def scrap_github():
    '''
        scrap github link and append all hyperlinks to a list
    '''
    url = github_link
    response = requests.get(url, headers=headers,timeout=timeout)
    soup = BeautifulSoup(response.content, "html.parser")
    all_links_tag = soup.find_all("a")
    all_links = []
    for each_link in all_links_tag:
        all_links.append(each_link["href"])
    query_str = get_query_string()
    search_query_str(all_links,query_str)

