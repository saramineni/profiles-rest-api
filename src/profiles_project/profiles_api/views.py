from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from . import serializers
from . import AIBot
from . import AIHelper
from . import models
from . import permissions
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

class refreshBotView(APIView):
    serializer_class = serializers.refreshSeralizer
    def put(self, request, pk=None):
        network = AIHelper.NeuralNetworks()
        try:
            network.intializeNetwork()
            return Response({'status':'success'})
        except Exception as e:
            print(e)
            return Response({'status':'unable to refresh the algorithm at this time'})

class testViewset(viewsets.ViewSet):

    serializer_class = serializers.HelloSerializer

    def list(self, request):

        a_viewset=[
            'adds more flexibility',
            'uses router functions from django framework',
        ]

        return Response({'message':'Hello there','a_view_set':a_viewset})

    def create(self,request):

        serializer = serializers.HelloSerializer(data= request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request, pk=None):

        return Response({'http_method':'GET'})

    def update(self, request, pk= None):

        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk = None):

        return Response({'http_method':'PATCH'})

    def destroy(self, request, pk=None):

        return Response({'http_method':'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):

    serializer_class= serializers.UserProfileSerializer
    queryset=models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes =(permissions.UpdateOwnProfile,)
