from unicodedata import name
from django.urls import path,include
from webapp.views import Song,SongDetails

urlpatterns=[
    # path('songs',getsongs,name="songs"),
    path('songs',Song.as_view(),name="songs"),
    path('songdetails',SongDetails.as_view(),name="songdetails")
]