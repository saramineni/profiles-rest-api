from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class HelloApiView(APIView):
    """testing api view"""


    def get(self, request, format = None):

        an_apiview=[
            'this is for logical processing',
            'this uses http methods',
            'this gives more freedom to communicate with other apis'
        ]

        return Response({"message":"Hello there","an_apiview":an_apiview})
