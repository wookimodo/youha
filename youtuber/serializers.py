from rest_framework import serializers
from .models import Youtuber,Comment



class YoutuberSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    imgUrl = serializers.CharField(max_length=500)
    link = serializers.CharField(max_length=500)
    subscribers = serializers.IntegerField(default=0)

    def create(self, validated_data):

        return Youtuber.objects.create(validated_data)

    def update(self, instance, validated_data):

        instance.id = validated_data.get('id', instance.id)
        instance.name = validated_data.get('name', instance.titnamele)
        instance.imgUrl = validated_data.get('imgUrl', instance.imgUrl)
        instance.link = validated_data.link('link', instance.link)
        instance.subscribers = validated_data.get('subscribers', instance.subscribers)
        instance.save()
        return instance
    
class CommentSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=100)
    videoId = serializers.CharField(max_length=100)
    author = serializers.CharField(max_length=100)
    comment = serializers.CharField(max_length=500)
    sentiment = serializers.CharField(max_length=30)
    score = serializers.FloatField(default=0)
    date = serializers.CharField(max_length=100)

    def create(self, validated_data):

        return Comment.objects.create(validated_data)

    def update(self, instance, validated_data):

        instance.name = validated_data.get('name', instance.name)
        instance.videoId = validated_data.get('videoId', instance.videoId)
        instance.author = validated_data.get('author', instance.author)
        instance.comment = validated_data.get('comment', instance.comment)
        instance.sentiment = validated_data.get('sentiment', instance.sentiment)
        instance.score = validated_data.get('score', instance.score)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance