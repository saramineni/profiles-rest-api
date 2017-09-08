from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers
# Create your views here.

class HelloApiView(APIView):
    """testing api view"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format = None):

        an_apiview=[
            'this is for logical processing',
            'this uses http methods',
            'this gives more freedom to communicate with other apis'
        ]

        return Response({"message":"Hello there","an_apiview":an_apiview})

    def post(self, request):

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello{0}'.format(name)
            return Response({'messsage':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
