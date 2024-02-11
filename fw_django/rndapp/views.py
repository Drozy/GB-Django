import logging
from random import randint, choice
from django.shortcuts import render, redirect
from .forms import GameForm

logger = logging.getLogger(__name__)


def log(view):
    def wrapper(request, *args, **kwargs):
        res = view(request, *args, **kwargs)
        logger.info(f'Function {view.__name__} returned "{res.content.decode("utf-8")}"')
        return res

    return wrapper


@log
def coin(request, count=1):
    results = [choice(['Орел', 'Решка']) for _ in range(count)]
    return render(request, 'rndapp/roll.html', {'game': 'Heads and tails', 'results': results})


@log
def dice(request, count=1):
    results = [f'Выпало {randint(1, 7)}' for _ in range(count)]
    return render(request, 'rndapp/roll.html', {'game': 'Dice roll', 'results': results})


@log
def rnd_num(request, count=1):
    results = [f'Выпало {randint(1, 100)}' for _ in range(count)]
    return render(request, 'rndapp/roll.html', {'game': 'Random number [1:100]', 'results': results})


def game_choice(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            game = form.cleaned_data['game']
            attempts = form.cleaned_data['attempts']
            if game == 'coin':
                return redirect(coin, count=attempts)
            if game == 'dice':
                return redirect(dice, count=attempts)
            if game == 'rnd_num':
                return redirect(rnd_num, count=attempts)
    else:
        form = GameForm()
    return render(request, 'rndapp/game_choice.html', {'form': form})
