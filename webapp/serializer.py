from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from webapp.models import song,songdetail

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model=song
        fields='__all__'

class SongDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=songdetail
        fields='__all__'