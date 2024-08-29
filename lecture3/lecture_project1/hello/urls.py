from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("guy", views.guy, name="guy"),
    path("patricia", views.patricia, name="patricia"),
    path("<str:name>", views.greet, name="greet")
]
