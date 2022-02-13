
from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """"Test API Views"""

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
