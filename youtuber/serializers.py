from rest_framework import serializers
from .models import Youtuber



class YoutuberSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    imgUrl = serializers.CharField(max_length=500)
    link = serializers.CharField(max_length=500)
    subscribers = serializers.IntegerField(default=0)

    def create(self, validated_data):

        # Create and return a new `Youtuber` instance, given the validated data.
        return Youtuber.objects.create(validated_data)

    def update(self, instance, validated_data):

        #Update and return an existing `Youtuber` instance, given the validated data.

        instance.name = validated_data.get('name', instance.titnamele)
        instance.imgUrl = validated_data.get('imgUrl', instance.imgUrl)
        instance.link = validated_data.link('link', instance.link)
        instance.subscribers = validated_data.get('subscribers', instance.subscribers)
        instance.save()
        return instance