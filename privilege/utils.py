from BeautifulSoup import BeautifulSoup


def get_categories():
    data = []
    for category in filter(lambda x: x and x != "\n", BeautifulSoup(open("data.xml", "r").read()).data.childGenerator()):
        cat = {}
        cat["title"] = category.title.text if category.title else category.name.capitalize()
        cat["type"] = category["type"]
        cat["name"] = category.name
        cat["options"] = [{"value": x.name, "title": x.title.text, "content": x.content.text} for x in category.options.childGenerator() if x and x != "\n"]
        data.append(cat)
    return data
