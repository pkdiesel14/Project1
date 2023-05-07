from django.shortcuts import render

from . import util



def display_page(request):
    pages = {
    CSS: "CSS.md",
    Django: "Django.md",
    Git: "Git.md"
}
    return render(request, "encyclopedia/entry.html", {
    "pages" : CSS
    })


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
