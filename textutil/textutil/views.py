from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def submitted(request):
    return render(request, 'submitted.html')

def feedback(request):
    return render(request, 'contact.html')

def analyse(request):
    djText = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    capitalize = request.POST.get('capitalize', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    extraspaceremove = request.POST.get('extraspaceremove', 'off')

    if removepunc != "on" and capitalize != "on" and newlineremove != "on" and extraspaceremove != "on":
        analysed = djText

    if removepunc == "on":
        analysed = ""
        panctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djText:
            if char not in panctuations:
                analysed = analysed + char
        djText = analysed

    if capitalize == "on":
        analysed = ""
        for char in djText:
            analysed = analysed + char.upper()
        djText = analysed

    if newlineremove == "on":
        analysed = ""
        for char in djText:
            if char != '\n' and char != '\r':
                analysed = analysed + char
        djText = analysed

    if extraspaceremove == "on":
        analysed = ""
        for index, char in enumerate(djText):
            if not(djText[index] == " " and djText[index+1] == " "):
                analysed = analysed + char
        djText = analysed

    params = {'analysed_text': analysed, 'purpose': 'Your expected text: '}
    return render(request, 'analyse.html', params)

def feedbacksubmit(request):
    djName = request.GET.get('fullname', 'default')
    djEmail = request.GET.get('email', 'default')
    djRadio = request.GET.get('flexRadioDefault', 'off')
    djSelect = request.GET.get('select', 'Select your Query about')
    djQuery = request.GET.get('query', 'default')
    djYourself = request.GET.get('yourself', 'default')
    return render(request, 'submitted.html')
