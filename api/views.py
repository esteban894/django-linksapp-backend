from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .models import Link
from .serializers import LinkSerializer
from .serializers import UserSerializer
from .authenticate import EmailPasswordAuthentication


@api_view(["GET"])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/links/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of links'
        },
        {
            'Endpoint': '/links/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single link object'
        },
        {
            'Endpoint': '/links/create/',
            'method': 'POST',
            'body':  {
                "title": "str",
                "link": "str",
                "description": "str"
            },
            'description': 'Creates new link with data sent in post request'
        },
        {
            'Endpoint': '/links/id/update/',
            'method': 'PUT',
            'body':  {
                "title": "str",
                "link": "str",
                "description": "str",
            },
            'description': 'Creates an existing link with data sent in post request'
        },
        {
            'Endpoint': '/links/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting link'
        },

        {
            'Endpoint': '/users/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of users'
        },
        {
            'Endpoint': '/users/id/',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single users'
        },
        {
            'Endpoint': '/users/id/create/',
            'method': 'POST',
            'body': {
                "username": "str",
                "password": "str",
                "email": "str",
            },
            'description': 'Create a new user with data sent in the post request'
        },
        {
            'Endpoint': '/users/id/update/',
            'method': 'PUT',
            'body': {
                "username": "str",
                "password": "str",
                "email": "str",
            },
            'description': 'Creates an existing user with data sent in post request'
        },
        {
            'Endpoint': '/users/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes an existing user'
        },
    ]
    return Response(routes, status=status.HTTP_200_OK)


@api_view(["GET"])
def getLinks(request):
    links = Link.objects.all()
    serializer = LinkSerializer(links, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def getLink(request, pk):
    link = Link.objects.get(id=pk)
    serializer = LinkSerializer(link, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["PUT"])
def updateLink(request, pk):
    data = request.data
    link = Link.objects.get(id=pk)
    serializer = LinkSerializer(instance=link, data=data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
def createLink(request):
    data = request.data
    link = Link.objects.create(
        title=data["title"], link=data["link"], description=data["description"])
    serializer = LinkSerializer(instance=link, many=False)
    return Response(serializer.data, status.HTTP_201_CREATED)


@api_view(["DELETE"])
def deleteLink(request, pk):
    link = Link.objects.get(id=pk)
    link.delete()
    return Response("Deleted link", status=status.HTTP_204_NO_CONTENT)


@api_view(["GET"])
def getUsers(request):
    user = User.objects.all()
    serializer = UserSerializer(user, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getUser(request, pk):
    user = User.objects.get(id=pk)
    if user:
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        raise Response('Does not exist the user',
                       status=status.HTTP_404_NOT_FOUND)


@api_view(["POST"])
def createUser(request):
    data = request.data
    data["password"] = make_password(data["password"])

    user = User.objects.create(
        username=data["username"],
        email=data["email"],
        password=data["password"])
    serializer = UserSerializer(instance=user, many=False)
    return Response(serializer.data, status.HTTP_201_CREATED)


@api_view(["PUT"])
def updateUser(request, pk):
    data = request.data
    data["password"] = make_password(data["password"])

    user = User.objects.get(id=pk)
    serializer = UserSerializer(instance=user, data=data)

    if serializer.is_valid():
        serializer.save()

    return Response("Updated data", status=status.HTTP_200_OK)


@api_view(["DELETE"])
def deleteUser(request, pk):
    user = User.objects.get(id=pk)
    user.delete()
    return Response("Deleted user", status=status.HTTP_204_NO_CONTENT)


@api_view(["POST"])
def authUser(request):
    EPAuth = EmailPasswordAuthentication()
    username, password = EPAuth.authenticate(request)

    if username and password:
        res = {"detail": "User authenticated"}
        return Response(res, status=status.HTTP_200_OK)
