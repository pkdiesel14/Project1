from django.urls import path

from . import views

# this list the functions that get called when the browser goes to the listed path
# example: when the browser points to /entry the function views.entry will be called
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("search/", views.search, name="search"),
    path("newpage/", views.newpage, name="newpage"),
    path("randomPage/", views.randomPage, name="randomPage"),
    path("edit_page/", views.edit_page, name="edit_page"),
    path("save_edit/", views.save_edit, name="save_edit"),

]
