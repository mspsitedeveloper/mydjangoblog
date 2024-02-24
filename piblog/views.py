from django.shortcuts import render
from django.shortcuts import HttpResponse

def about(request):
    # return HttpResponse('hello mother')
    return render(request , 'about.html')
def home(request):
    # return HttpResponse('welcome to piblog')
    return render(request , 'home.html')