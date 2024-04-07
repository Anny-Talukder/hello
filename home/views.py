from django.shortcuts import render, HttpResponse

def index(request):
    context = {
        'variable1': "this is sent",
        'variable2': "That was sent"
    }
    return render(request, 'index.html', context)
def about(request):
    return HttpResponse("This is about page")

def services(request):
    return HttpResponse("This is services page")

def contact(request):
    return HttpResponse("This is contact page")