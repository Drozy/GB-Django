from django import forms


class GameForm(forms.Form):
    game = forms.ChoiceField(choices=[('coin', 'Монетка'), ('dice', 'Кубик'), ('rnd_num', 'Случайное число')])
    attempts = forms.IntegerField(min_value=1, max_value=64)
