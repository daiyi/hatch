from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {'message': "Hello egg"}
    return render(request,'incubator.html', context)
