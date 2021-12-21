from django.http.response import HttpResponse
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')
    # return HttpResponse('Home')


def analyze(request):
    djtext = request.POST.get('text')
    print(djtext)
    removepunc = request.POST.get('removepunc', 'off')
    removespace = request.POST.get('removespace', 'off')
    removenewline = request.POST.get('removenewline', 'off')
    allcaps = request.POST.get('allcaps', 'off')

    if removepunc == 'on':
        analyzed = ""
        punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuation:
                analyzed = analyzed + char
        params = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if (removespace == 'on'):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Remove Extra Space', 'analyzed_text': analyzed}
        djtext = analyzed

    if (removenewline == 'on'):
        analyzed = ""
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char
        params = {'purpose': 'Remove New Lines', 'analyzed_text': analyzed}

    if(allcaps == 'on'):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'All Capitalize', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    if(removepunc != 'on' and removenewline != 'on' and removespace != 'on' and allcaps != 'on'):
        # return HttpResponse('Please select any operation')
        return render(request, 'error.html')

    return render(request, 'analyze.html', params)
