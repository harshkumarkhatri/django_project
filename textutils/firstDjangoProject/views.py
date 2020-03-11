

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def first(request):
    return HttpResponse('first page')

def about(request):
    djtext=(request.POST.get('text','default'))
    removepunc=(request.POST.get('removepunc','off'))
    fullcaps=(request.POST.get('fullcaps','off'))
    newlineremover=(request.POST.get('newlineremover','off'))
    extraspaceremover=(request.POST.get('extraspaceremover','off'))
    charactercounter=(request.POST.get('charactercounter','off'))
    if removepunc=='on':
        analyzed=""
        punctuations='''!(){}[];:'"\,.<>/?@#$%&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'Remove punc','analyzed_text':analyzed}
        djtext=analyzed
    if fullcaps=="on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params={'purpose':'making uppercase','analyzed_text':analyzed}
        djtext=analyzed
    if newlineremover=='on':
        analyzed=""
        for char in djtext:
            if char!='\n' and char!="\r":
                analyzed=analyzed+char
        params={'purpose':'removed new lines','analyzed_text':analyzed}
        djtext=analyzed
    if extraspaceremover=='on':
        analyzed=""
        for index,char in enumerate(djtext):
            if not djtext[index]=="" and djtext[index+1]==" ":
                analyzed=analyzed+char
        params={'purpose':'removinbg extra spaces','analyzed_text':analyzed}
        djtext=analyzed
    if charactercounter=='on':
        analyzed=""
        count=0
        for index,char in enumerate(djtext):
            count=index
        params={'purpose':'character counter','analyzed_text':str(count+1),'count':'true'}
    if (removepunc!='on' and charactercounter!='on' and extraspaceremover!='on' and newlineremover!='on' and fullcaps!="on"):
        HttpResponse('Plz select an option.')


    return render(request,'analyze.html',params)

