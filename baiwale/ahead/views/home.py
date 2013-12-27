# -*- coding: utf-8 -*-
from ..utils.lazy import *
from ..models import Thing, Category

def index(request):
    things = Thing.objects.all().order_by('-created_at')
    return render(request, "index.html", {'current': 'home', 'things': things})


def whale(request, menu):
    things = get_object_or_404(Category, title=menu).thing_set.all().order_by('-created_at')
    return render(request, "whale/index.html", {'current': menu, 'things': things})


def show(request, id):
    whale = get_object_or_404(Thing, id=id)
    return render(request, "whale/show.html", {'current': whale.category.title,'whale': whale})


def about(request):
    return render(request, "whale/about.html", {'current': 'about'})