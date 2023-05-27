from django.shortcuts import render
from PyDictionary import PyDictionary
import requests
from bs4 import BeautifulSoup


def synonyms(term):
    response = requests.get('https://www.thesaurus.com/browse/{}'.format(term))
    soup = BeautifulSoup(response.text, 'lxml')
    soup.find('section', {'class': 'css-17ofzyv e1ccqdb60'})
    return [span.text for span in soup.findAll('a', {'class': 'css-1kg1yv8 eh475bn0'})]


def index(request):
    return render(request,'index.html')


def word(request):
    search = request.GET.get('search')
    dictionary = PyDictionary()
    meaning = dictionary.meaning(search)
    synonym = synonyms(search)
    #antonym = antonyms(search)
    context = {
        'search' : search.capitalize(),
        'meaning' : meaning['Noun'][0],
        'synonym' : synonym,
        #'antonym' : antonym
    }
    return render(request, 'word.html',context)
