# I have created this file
from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    return render(request,'index.html')

def analyse(request):
    # get the text
    djtext = request.POST.get('text','default')
    backup = djtext
    # check the checkbox value

    fullcaps = request.POST.get('fullcaps','off')
    removepunc = request.POST.get('removepunc', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charactercount = request.POST.get('charactercount', 'off')

    # check if the checkbox is on

    # 1. remove punctuations
    if removepunc == 'on':
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analysed = ""
        for c in djtext:
            if c not in punctuations:
                analysed+=c
        params = {
            'purpose':'Punctuations removed',
            'analysed_text': analysed
        }
        djtext = analysed


    # 2. capitalize all
    if fullcaps == 'on':
        analysed = ''
        for c in djtext:
            analysed+=c.upper()
        params = {
            'purpose': 'Full Caps',
            'analysed_text': analysed
        }
        djtext = analysed

    # 3. New line remover
    if newlineremover == 'on':
        analysed = ''
        for c in djtext:
            if c != '\n':
                analysed+=c
        params = {
            'purpose': 'new line removed',
            'analysed_text': analysed
        }
        djtext = analysed

    # 4 . extra space remover
    if extraspaceremover == 'on':
        list_of_words = djtext.split()

        x = [word for word in list_of_words if word is not ' ']

        analysed = ' '.join(x)

        params = {
            'purpose': 'new line removed',
            'analysed_text': analysed
        }
        djtext = analysed

        # 5. character count
    if charactercount == 'on':
        analysed =str(len(djtext))
        params = {
            'purpose': 'new line removed',
            'analysed_text': analysed
        }
    if removepunc=='off' and extraspaceremover=='off' and newlineremover=='off' and fullcaps=='off' and charactercount=='off':
        return HttpResponse(djtext)
    elif removepunc == 'on' and extraspaceremover == 'on' and newlineremover == 'on' and fullcaps == 'on' and charactercount == 'on':
        return render(request,'analyze.html', {
            'purpose': 'All',
            'analysed_text': 'you have selected all ,\n Your Text : ' + backup
        })
    return render(request, 'analyze.html', params)

