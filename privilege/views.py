from BeautifulSoup import BeautifulSoup
from django.shortcuts import render


def index(request):
    data = []
    for category in filter(lambda x: x and x != "\n", BeautifulSoup(open("data.xml", "r").read()).data.childGenerator()):
        cat = {}
        cat["title"] = category.title.text
        cat["type"] = category["type"]
        cat["options"] = [{"value": x.name, "title": x.title.text} for x in category.options.childGenerator() if x and x != "\n"]
        data.append(cat)
    return render(request, "index.haml", {"privileges": data})
