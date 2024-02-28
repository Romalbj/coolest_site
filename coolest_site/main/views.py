from django.shortcuts import render
from django.http import HttpResponse

def output(request):
    return render(request, 'main/output.html')

def about(request):
    return render(request, 'main/about.html')

def works(request):
    return render(request, 'main/works.html')

def plans(request):
    return render(request, 'main/plans.html')

