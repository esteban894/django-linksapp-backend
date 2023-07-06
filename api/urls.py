from django.urls import path
from . import views

urlpatterns = [
    path("", views.getRoutes, name="routes"),
    path("links/", views.getLinks, name="links"),
    path("links/<int:pk>/update/", views.updateLink, name="update-link"),
    path("links/create/", views.createLink, name="add-link"),
    path("links/<int:pk>/delete/", views.deleteLink, name="delete-link"),
    path("links/<int:pk>/", views.getLink, name="link"),

    path("users/", views.getUsers, name="users"),
    path("users/<int:pk>/update/", views.updateUser, name="update-user"),
    path("users/create/", views.createUser, name="create-user"),
    path("users/<int:pk>/delete/", views.deleteUser, name="delete-user"),
    path("users/<int:pk>/", views.getUser, name="user"),
    path("users/authuser/", views.authUser, name="auth-user"),
]
