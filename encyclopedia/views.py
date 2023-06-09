from django.shortcuts import render

from . import util
import markdown2
import random




# inside the {} are the variables we are passing to the html page
# the text inside the "" is the variable name inside the web page
# and the text after the : is the source of the data being passed

def convert_md_to_html(title):
    content = util.get_entry(title)
    if content == None:
        return None
    else:
        return markdown2.markdown(content)



def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),                             
    })

def entry(request, title):
    html_content = convert_md_to_html(title)
    if html_content == None:
        return render(request, "encyclopedia\error.html")
    else:
        return render(request, "encyclopedia\entry.html", {"content": html_content, 
    "title": title
    })

def search(request):
    if request.method == "POST":
        entry_search = request.POST['q']
        html_content = convert_md_to_html(entry_search)
        if html_content is not None:
           return render(request, "encyclopedia\entry.html", {
           "content": html_content, 
           "title": entry_search 
           })
        else:
            mdlist = util.list_entries()
            results = []
            for item in mdlist:
                if entry_search.lower() in item.lower():
                    results.append(item)
            return render(request, "encyclopedia/search.html", {
                "results": results,
                "title":entry_search
            })
    return 

def newpage(request):
    if request.method == "GET":
        return render(request, "encyclopedia/newpage.html")
    else:
        title = request.POST['title']
        content = request.POST['content']
        titleExits = util.get_entry(title)
        print(f"Title exists is: {titleExits}")
        if titleExits is not None:
            print("Title already exists")
            return render(request, "encyclopedia/error.html", {
            "message": "Title already exists"
            })
        else:
            util.save_entry(title, content)
            html_content = convert_md_to_html(title)
            return render(request, "encyclopedia/entry.html", {
                "title":title,
                "content":html_content
            })
        
def randomPage(request):
    mdlist = util.list_entries()
    selection = random.choice(mdlist)
    html_content = convert_md_to_html(selection)
    return render(request, "encyclopedia/entry.html", {
        "title": selection,
        "content":html_content
    })

def edit_page(request):
    if request.method == 'POST':
        title = request.POST['entry_title']
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {
            "title": title,
            "content": content
        })
    
def save_edit(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        util.save_entry(title, content)
        html_content = convert_md_to_html(title)
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": html_content
        })