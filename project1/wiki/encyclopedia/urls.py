from django.urls import path

from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("new_page", views.new_page, name="new_page"),
    path("edit", views.edit, name="edit"),
    path("random", views.random, name="random"),
    path("<str:name>", views.entry, name="entry")
]
