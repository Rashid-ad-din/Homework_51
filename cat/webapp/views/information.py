from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from webapp.cat import Cat
from webapp.db import DB


def cat_view(request: WSGIRequest):
    if request.method == 'GET':
        if request.GET.get('action') == 'play':
            DB.cat.play()
        elif request.GET.get('action') == 'eat':
            if DB.cat.state == 'sleep':
                text = DB.cat.state_fun()
                return return_response(request, text)
            DB.cat.eat()
        elif request.GET.get('action') == 'sleep':
            DB.cat.set_state('sleep')
        text = DB.cat.state_fun()
        return return_response(request, text)
    Cat.add_cat(request)
    text = DB.cat.state_fun()
    return return_response(request, text)


def return_response(request, text):
    return render(request, 'information.html', context={
        'cat': DB.cat,
        'img': DB.get_image(DB.cat),
        'text': text
    })
