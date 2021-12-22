import requests
from bs4 import BeautifulSoup


def get_scraping():
    result_count =0
    URL = 'https://en.wikipedia.org/wiki/History_of_Mexico'
    # print(URL)
    page = requests.get(URL)
    # print(page.content)
    soup = BeautifulSoup(page.content,'html.parser')
    # print(soup)
    results_paragraph = soup.find_all('p')    
    results_citation = soup.find_all(title='Wikipedia:Citation needed')
    phrases = []
    result_count = 0

    for paragraph in results_paragraph:       
        result_count +=1
        print(paragraph)
        phrases.append(paragraph)
    # print(results_citation)
    print(result_count)
    # citations_required = results.find_all(title='Wikipedia:Citation needed')
    # print(citations_required)
    



    

def get_citations_needed():
    pass

def get_citations_needed_count():
    citations = get_scraping()
    print(citations)

get_citations_needed_count()