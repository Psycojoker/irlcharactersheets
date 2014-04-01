from django.shortcuts import render
from .utils import get_categories


def index(request):
    return render(request, "index.haml", {"privileges": get_categories()})


def sheet(request):
    print request.GET
    return render(request, "sheet.haml")
