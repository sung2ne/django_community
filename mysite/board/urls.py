from django.urls import path

from board import views

app_name = "board"

urlpatterns = [
    path("", views.board_list, name="list"),
    path("create/", views.board_create, name="create"),
    path("<int:board_id>/", views.board_read, name="read"),
    path("<int:board_id>/delete/", views.board_delete, name="delete"),
    path("<int:board_id>/update/", views.board_update, name="update"),
]