from django.shortcuts import render
from django.http import HttpResponse

def output(request):
    return render(request, 'main/output.html')

def about(request):
    return render(request, 'main/about.html')

def works(request):
    return render(request, 'main/works.html')

def beauty(request):
    return render(request, 'main/beauty.html')

