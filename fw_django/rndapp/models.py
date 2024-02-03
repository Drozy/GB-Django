"""
Задание №1
📌 Создайте модель для запоминания бросков монеты: орёл или решка.
📌 Также запоминайте время броска

Задание №2
📌 Добавьте статический метод для статистики по n последним броскам монеты.
📌 Метод должен возвращать словарь с парой ключей-значений, для орла и для решки.
"""
from django.db import models
from random import choice


class CoinToss(models.Model):
    SIDES = ('head', 'tail')
    side = models.CharField(max_length=10, default=choice(SIDES))
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Монета упала стороной "{self.side}"'

    @staticmethod
    def get_tosses(n=None):
        if n is None:
            n = 0
        tosses = CoinToss.objects.all()[-n:]
        heads_count = sum(coin.side == 'head' for coin in tosses)
        tails_count = n - heads_count
        return {'heads_count': heads_count, 'tails_count': tails_count}
