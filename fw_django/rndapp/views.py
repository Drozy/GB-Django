import logging
from random import randint, choice
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def log(view):
    def wrapper(request, *args, **kwargs):
        res = view(request, *args, **kwargs)
        logger.info(f'Function {view.__name__} returned "{res.content.decode("utf-8")}"')
        return res
    return wrapper


# Create your views here.

@log
def coin(request):
    return HttpResponse(f"Выпало {choice(['Орел', 'Решка'])}")


@log
def dice(request):
    return HttpResponse(f"Выпало {randint(1, 6)}")


@log
def rnd_num(request):
    return HttpResponse(f"Выпало {randint(1, 100)}")
