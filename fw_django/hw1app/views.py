from django.http import HttpResponse

from hw1app.variables import index_data, about_data


# Create your views here.
def index(request):
    return HttpResponse(index_data)


def about(request):
    return HttpResponse(about_data)
