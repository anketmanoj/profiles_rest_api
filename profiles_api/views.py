from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers


class HelloApiView(APIView):
    """"Test API Views"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """"Returns a list of API Views Features"""
        an_apiview = [
            'Uses HTTP Methods as functions(get, post, patch, put, delete)',
            'Is similar to a traditional Django view',
            'Gives you the most control over your application logic',
            'is mapped manually to urls',
        ]

        return Response({
            'message': 'Hello',
            'an_apiview': an_apiview,
        })

    def post(self, request):
        """"Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hello, the name is {name}"
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """"Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update on an object"""
        return Response({'method': "PATCH"})

    def delete(self, request, pk=None):
        """"Delete an object"""
        return Response({'method': "DELETE"})


class HelloViewSet(viewsets.ViewSet):
    """Test API Viewset"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """"Return a hello message"""
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update, destroy)',
            'Automatically maps to urls using routers',
            'Provides more functionality with less code',
        ]
        return Response({'message': "Hello", 'a_viewset': a_viewset})

    def create(self, request):
        """Create a New hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hello, name viewset {name}"
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handle getting an object by its id"""
        return Response({'method': "GET"})

    def update(self, request, pk=None):
        """??pdates the entire object"""
        return Response({'method': "PUT"})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""
        return Response({'method': "PATCH"})

    def destroy(self, request, pk=None):
        """"Handle removing an object"""
        return Response({'method': "DELETE"})
