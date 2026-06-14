from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("add/", views.add_task, name="add_task"),
    path("complete/<int:task_id>/", views.complete_task, name="complete_task"),
]