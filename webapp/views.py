from dataclasses import fields
from unittest import result
from venv import create
from django.http import HttpResponse
from rest_framework.views import Response
from django.shortcuts import render
from webapp.serializer import SongSerializer,SongDetailSerializer
from webapp.models import song,songdetail
from django.http.response import JsonResponse
from rest_framework.views import APIView

from django.core import serializers
from django.db import connection
import json
import collections

# Create your views here.
# def getsongs(request):
#     songlist=song.objects.all()
#     serializer=SongSerializer(songlist,many=True)
#     return JsonResponse(serializer.data,safe=False)

class Song(APIView):
    def get(self,request,*args,**kwargs):
        songlist=song.objects.order_by('-worship_date').all()
        serializer=SongSerializer(songlist,many=True)
        return Response(serializer.data)

    
    def post(self,request,*args,**kwargs):
        song_data=request.data
        new_song=song.objects.create(
            songname=song_data["songname"],worship_date=song_data["worship_date"],updated_date=song_data["updated_date"]
        )

        serializer_song=SongSerializer(new_song)
        print(new_song.id)
        song_order_detail=song_data["songdetail"].split(";-") #splitting on the basis of ;-
       
        for paragraph in song_order_detail:
            if paragraph:
                songdetail_id=AddSongDetail(new_song,(song_order_detail.index(paragraph)+1),paragraph)
      
        return Response(serializer_song.data)

    def delete(self,request,*args,**kwargs):
        song_id=request.data["song_id"]
        result=song.objects.filter(id=song_id).delete()
        # result=song.objects.all().delete()
        print(result)
        return Response({"Record deleted successfully"})



def AddSongDetail(new_song,ordernum,songdetails):
    new_songdetail=songdetail.objects.create(
        song_id=new_song,order=ordernum,song_text=songdetails.strip()
    )
    return new_songdetail.id



class SongDetails(APIView):
    def get(self,request,*args,**kwargs):
        songid=request.data["song_id"]
        songs=songdetail.objects.filter(song_id__id=songid).order_by('order').all()
        data=serializers.serialize('json',songs)
        return HttpResponse(data,content_type="application/json")

        # song_detail=songdetail.objects.all()
        # serializer=SongDetailSerializer(song_detail,many=True)
        # return Response(serializer.data)
    
    def delete(self,request,*args,**kwargs):
        result=song.objects.delete()
        return Response({"Record deleted successfully"})