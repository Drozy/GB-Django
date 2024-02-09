from django.shortcuts import render
from hw1app.variables import index_data, about_data


def index(request):
    return render(request, 'hw1app/base.html', {'title': 'Main page', 'content': index_data})


def about(request):
    return render(request, 'hw1app/base.html', {'title': 'About', 'content': about_data})
