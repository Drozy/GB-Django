from django.http import HttpResponse


# Create your views here.
def index(request):
    data = ('<!DOCTYPE html>'
            '<html lang="en">'
            '<head>'
            '<meta charset="UTF-8" />'
            '<meta name="viewport" content="width=device-width, initial-scale=1.0" />'
            '<title>HW1 - Main</title>'
            '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" '
            'integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" '
            'crossorigin="anonymous">'
            '</head>'
            '<body>'
            '<div class="container">'
            '<nav class="nav">'
            '<a class="nav-link active" href="/">Главная</a>'
            '<a class="nav-link" href="/about">О себе</a>'
            '</nav>'
            '<h1>Главная страница</h1>'
            '<p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Esse repellat'
            'libero deserunt recusandae! Atque consequuntur totam vel inventore maiores'
            'dolore tempore, id delectus aliquam quasi reiciendis alias at dolores'
            'voluptates.</p>'
            '<h2>Добро пожаловать на сайт</h2>'
            '<p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Esse repellat'
            'libero deserunt recusandae! Atque consequuntur totam vel inventore maiores'
            'dolore tempore, id delectus aliquam quasi reiciendis alias at dolores'
            'voluptates.</p>'
            '</div></body></html>')
    return HttpResponse(data)


def about(request):
    data = ('<!DOCTYPE html>'
            '<html lang="en">'
            '<head>'
            '<meta charset="UTF-8" />'
            '<meta name="viewport" content="width=device-width, initial-scale=1.0" />'
            '<title>HW1 - About</title>'
            '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" '
            'integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" '
            'crossorigin="anonymous">'
            '</head>'
            '<body>'
            '<div class="container">'
            '<nav class="nav">'
            '<a class="nav-link" href="/">Главная</a>'
            '<a class="nav-link active" href="/about">О себе</a>'
            '</nav>'
            '<h1>О себе</h1>'
            '<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eaque architecto, fuga laborum rerum '
            'expedita velit quis exercitationem, sed fugit soluta deserunt ratione esse dignissimos neque quas '
            'nostrum molestias doloremque consequatur voluptate explicabo aliquam iusto natus perspiciatis! '
            'Voluptates voluptas officia praesentium officiis. Natus fugit autem impedit alias consectetur '
            'minus et voluptates, doloribus itaque? Illo ea aperiam exercitationem natus in unde fugiat sit '
            'quod hic! Quidem eveniet accusamus error facere nostrum facilis esse eum minima cum accusantium '
            'temporibus modi, sequi quaerat odio aliquam dolores asperiores aut veritatis at eaque? Tenetur '
            'pariatur minus repellat reprehenderit, quibusdam illum! Eligendi ipsam est nobis unde iste.</p>'
            '</div></body></html>')
    return HttpResponse(data)
