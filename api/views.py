from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Link
from .serializers import LinkSerializer


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
                "title": "",
                "link": "",
                "description": ""
            },
            'description': 'Creates new link with data sent in post request'
        },
        {
            'Endpoint': '/links/id/update/',
            'method': 'PUT',
            'body':  {
                "title": "",
                "link": "",
                "description": ""
            },
            'description': 'Creates an existing link with data sent in post request'
        },
        {
            'Endpoint': '/links/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting link'
        },
    ]
    return Response(routes)


@api_view(["GET"])
def getLinks(request):
    links = Link.objects.all()
    serializer = LinkSerializer(links, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getLink(request, pk):
    link = Link.objects.get(id=pk)
    serializer = LinkSerializer(link, many=False)
    return Response(serializer.data)


@api_view(["PUT"])
def updateLink(request, pk):
    data = request.data
    link = Link.objects.get(id=pk)
    serializer = LinkSerializer(instance=link, data=data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(["POST"])
def createLink(request):
    data = request.data
    link = Link.objects.create(
        title=data["title"], link=data["link"], description=data["description"])
    serializer = LinkSerializer(instance=link, many=False)
    return Response(serializer.data)


@api_view(["DELETE"])
def deleteLink(request, pk):
    link = Link.objects.get(id=pk)
    link.delete()
    return Response("El link se ha borrado")
