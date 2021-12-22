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

    results = soup.find_all('p')
    print(results)
    for result in results:
        result_count +=1
    # citations_required = results.find_all(title='Wikipedia:Citation needed')
    # print(citations_required)
    return result_count



    

def get_citations_needed():
    pass

def get_citations_needed_count():
    citations = get_scraping()
    print(citations)

get_citations_needed_count()