from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
    return render(request, 'home.html',)

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    worddict = {}

    for word in wordlist:
        #how many times the word appears
        if word in worddict:
            #Increase
            worddict[word] += 1
        else:
            #value equals one
            worddict[word] = 1
    #reverse=True lower   operator several grades ok
    sortedwords = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist), 'worddict': sortedwords,})

def about(request):
    return render(request, 'about.html',)
