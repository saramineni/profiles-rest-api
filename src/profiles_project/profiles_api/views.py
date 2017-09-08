from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers
from . import AIBot
# Create your views here.

class InternalBotView(APIView):
    """testing api view"""
    serializer_class = serializers.inputSerializer
    def get(self, request, format = None):

        an_apiview=[
            'this is for logical processing',
            'this uses http methods',
            'this gives more freedom to communicate with other apis'
        ]

        return Response({"message":"get call","an_apiview":an_apiview})

    def post(self, request):
        serializer = serializers.inputSerializer(data=request.data)
        network = AIBot.demoNetwork()
        if serializer.is_valid():
            inMessage = str(serializer.data.get('inpMessage'))
            botResponse = network.getResponse(message=inMessage)
            return Response({'messsage':botResponse})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
