from rest_framework import serializers
from . models import New
from taggit.serializers import TagListSerializerField, TaggitSerializer

class NewSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = New
        fields = '__all__'
