from django.shortcuts import render
from django.http import HttpResponse

def output(request):
    return HttpResponse('Здорова,чепух')

