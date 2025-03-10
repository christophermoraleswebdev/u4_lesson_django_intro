from django.shortcuts import render
from .models import Artist, Song
from rest_framework import generics 
from .serializers import ArtistSerializer, SongSerializer

# Create your views here.

class ArtistList(generics.ListCreateAPIView):
      queryset = Artist.objects.all()
      serializer_class = ArtistSerializer


class ArtistDetail(generics.RetrieveUpdateDestroyAPIView):
      queryset = Artist.objects.all()
      serializer_class = ArtistSerializer

class SongList(generics.ListCreateAPIView):
      queryset = Song.objects.all()
      serializer_class = SongSerializer

class SongDetail(generics.RetrieveUpdateDestroyAPIView):
      queryset = Song.objects.all()
      serializer_class = SongSerializer