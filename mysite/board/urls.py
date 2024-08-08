from django.urls import path

from board import views

app_name = "board"

urlpatterns = [
    path("", views.board_list, name="list"),
    path("create/", views.board_create, name="create"),
]