from rest_framework import serializers

class HelloSerializer(serializers.Serializer):

    name= serializers.CharField(max_length=255)

class inputSerializer(serializers.Serializer):

    inpMessage = serializers.CharField(max_length=255)
    order = serializers.IntegerField()
