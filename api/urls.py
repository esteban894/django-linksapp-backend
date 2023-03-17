from django.urls import path
from . import views

urlpatterns = [
    path("", views.getRoutes, name="routes"),
    path("links/", views.getLinks, name="links"),
    path("links/<str:pk>/update/", views.updateLink, name="update-link"),
    path("links/create/", views.createLink, name="add-link"),
    path("links/<str:pk>/delete/", views.deleteLink, name="add-link"),

    path("links/<str:pk>", views.getLink, name="link"),
]
