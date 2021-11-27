from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from rest_framework import permissions


from .models import Series,Movie,User,BorrowedMovies,BorrowedSeries,Subtitles, EpisodeData
from .serializers import SeriesSerializer,MovieSerializer,UserSerializer,BorrowedSeriesSerializer,\
    BorrowedMoviesSerializer,SubtitlesSerializer,EpisodeDataSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the a index.")
# Create your views here.
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'
    permission_classes = [IsAuthenticated,IsAdminUser]

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'
    permission_classes = [IsAuthenticated,IsAdminUser]

class SeriesList(generics.ListCreateAPIView):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer
    name = 'series-list'
    filter_fields = ['title','publicationDate','originalLanguage','startDate','broadcaster']
    search_fields = ['title','broadcaster']
    ordering_fields = ['title','startDate','broadcaster']
    permission_classes = [IsAuthenticated]

class SeriesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer
    name = 'series-detail'
    permission_classes = [IsAuthenticated]

class EpisodeDataList(generics.ListCreateAPIView):
    queryset = EpisodeData.objects.all()
    eiaserializer_class = EpisodeDataSerializer
    filter_fields = ['seasonNumber', 'episodeNumber', 'title']
    search_fields = ['seasonNumber', 'episodeNumber', 'title']
    ordering_fields = ['seasonNumber', 'episodeNumber', 'title']
    name = 'episodedata-list'
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class EpisodeDataDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EpisodeData.objects.all()
    serializer_class = EpisodeDataSerializer
    name = 'episodedata-detail'
    permission_classes = [IsAuthenticated]


class MovieList(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    name = 'movie-list'
    filter_fields = ['title', 'publicationDate', 'originalLanguage', 'genre', 'director', 'countryOfOrigin', 'producer']
    search_fields = ['title', 'director']
    ordering_fields = ['title', 'publicationDate', 'director']
    permission_classes = [IsAuthenticated]

class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    name = 'movie-detail'
    permission_classes = [IsAuthenticated]

class BorrowedMoviesList(generics.ListCreateAPIView):
    queryset = BorrowedMovies.objects.all()
    serializer_class = BorrowedMoviesSerializer
    permission_classes = [IsAuthenticated]
    name = 'borrowedmovies-list'

class BorrowedMoviesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BorrowedMovies.objects.all()
    serializer_class = BorrowedMoviesSerializer
    permission_classes = [IsAuthenticated]
    name = 'borrowedmovies-detail'

class BorrowedSeriesList(generics.ListCreateAPIView):
    queryset = BorrowedSeries.objects.all()
    serializer_class = BorrowedSeriesSerializer
    permission_classes = [IsAuthenticated]
    name = 'borrowedseries-list'

class BorrowedSeriesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BorrowedSeries.objects.all()
    serializer_class = BorrowedSeriesSerializer
    permission_classes = [IsAuthenticated]
    name = 'borrowedseries-detail'

class SubtitlesList(generics.ListCreateAPIView):
    queryset = Subtitles.objects.all()
    serializer_class = SubtitlesSerializer
    permission_classes = [IsAuthenticated]
    name = 'subtitles-list'

class SubtitlesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subtitles.objects.all()
    serializer_class = SubtitlesSerializer
    permission_classes = [IsAuthenticated]
    name = 'subtitles-detail'

class EpisodeDataList(generics.RetrieveUpdateDestroyAPIView):
    queryset = EpisodeData.objects.all()
    serializer_class = EpisodeDataSerializer
    permission_classes = [IsAuthenticated]
    name = 'subtitles-list'

class EpisodeDataDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EpisodeData.objects.all()
    serializer_class = EpisodeDataSerializer
    permission_classes = [IsAuthenticated]
    name = 'subtitles-detail'

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    permission_classes = [IsAuthenticated]
    def get(self,request,*args,**kwargs):
        return Response({
            'status': 'request was permitted',
            'users': reverse(UserList.name,request=request),
            'series': reverse(SeriesList.name,request=request),
            'movies': reverse(MovieList.name, request=request),
            'borrowedmovies': reverse(BorrowedMoviesList.name, request=request),
            'borrowedseries': reverse(BorrowedSeriesList.name, request=request),
            'subtitles': reverse(SubtitlesList.name, request=request),
            'episodedata': reverse(EpisodeDataList.name, request=request),

        })