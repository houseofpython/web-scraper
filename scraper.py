import requests
from bs4 import BeautifulSoup


url = "https://en.wikipedia.org/wiki/History_of_Georgia_(U.S._state)"

#takes in a url string and returns an integer.
def get_citations_needed_count(url):

    req = requests.get(url)
    markup = req.text
    soup = BeautifulSoup(markup, 'html.parser')
    citations = soup.find_all('sup', {'class': 'noprint Inline-Template Template-Fact'})
    num_citations = len(citations)
    print('citations', citations)
    #return num_citations

#Takes in a url string and returns a report string
def get_citations_needed_report(url):
    report = ''
    req = requests.get(url)
    markup = req.text
    soup = BeautifulSoup(markup, 'html.parser')
    citations = soup.find_all('sup', {'class': 'noprint Inline-Template Template-Fact'})
    for p in citations:
        paragraph = p.find_parent('p')
        report += str(paragraph)
    return report




if __name__ == '__main__':
    url = "https://en.wikipedia.org/wiki/History_of_Georgia_(U.S._state)"
    print(get_citations_needed_report(url))
    print(get_citations_needed_count(url))




