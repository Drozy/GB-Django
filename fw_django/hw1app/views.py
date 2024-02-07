from django.shortcuts import render


def index(request):
    return render(request, 'hw1app/index.html')


def about(request):
    return render(request, 'hw1app/about.html')
