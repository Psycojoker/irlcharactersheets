from django.shortcuts import render
from .utils import get_categories


def index(request):
    return render(request, "index.haml", {"privileges": get_categories()})


def sheet(request):
    data = get_categories()
    new_data = []
    for i in data:
        p = i.copy()
        p["choice"] = {x["value"]: x.copy() for x in p["options"]}[request.GET[p["name"]]]
        p["others"] = filter(lambda x: x["value"] != request.GET[p["name"]], i["options"])
        new_data.append(p)
    return render(request, "sheet.haml", {"categories": new_data})
