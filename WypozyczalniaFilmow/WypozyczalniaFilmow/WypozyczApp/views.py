from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

from django_filters import AllValuesFilter,DateTimeFilter,NumberFilter,FilterSet

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
class UserFilter(FilterSet):
    min_accessLevel = NumberFilter(field_name='accessLevel', lookup_expr='gte')
    max_accessLevel = NumberFilter(field_name='accessLevel', lookup_expr='lte')
    login = AllValuesFilter(field_name='login')

    class Meta:
        model = User
        fields = ['min_accessLevel','max_accessLevel','login']

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'
    search_fields = ['login','dateOfBirth']
    ordering_fields = ['login','dateOfBirth','accessLevel']
    filter_class = UserFilter
    permission_classes = [IsAuthenticated,IsAdminUser]

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'
    permission_classes = [IsAuthenticated,IsAdminUser]

class SeriesFilter(FilterSet):
    from_startDate = DateTimeFilter(field_name='startDate',lookup_expr='gte')
    to_startDate = DateTimeFilter(field_name='startDate',lookup_expr='lte')

    class Meta:
        model = Series
        fields = ['from_startDate','to_startDate']


class SeriesList(generics.ListCreateAPIView):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer
    name = 'series-list'
    filter_fields = ['title','publicationDate','originalLanguage','startDate','broadcaster']
    search_fields = ['title','broadcaster']
    ordering_fields = ['title','startDate','broadcaster']
    permission_classes = [IsAuthenticated]
    filter_class = SeriesFilter

class SeriesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer
    name = 'series-detail'
    permission_classes = [IsAuthenticated]

class MovieFilter(FilterSet):
    from_publication_date = DateTimeFilter(field_name='publicationDate',lookup_expr='gte')
    to_publication_date = DateTimeFilter(field_name='publicationDate',lookup_expr='lte')

    class Meta:
        model = Movie
        fields = ['from_publication_date','to_publication_date']


class MovieList(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_class = MovieFilter
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

class BorrowedMoviesFilter(FilterSet):
    borrowed_date_from = DateTimeFilter(field_name='borrowedDate', lookup_expr='gte')
    borrowed_date_to = DateTimeFilter(field_name='borrowedDate', lookup_expr='lte')

    class Meta:
        model = BorrowedMovies
        fields = ['borrowed_date_from','borrowed_date_to']

class BorrowedMoviesList(generics.ListCreateAPIView):
    queryset = BorrowedMovies.objects.all()
    serializer_class = BorrowedMoviesSerializer
    permission_classes = [IsAuthenticated]
    filter_class = BorrowedMoviesFilter
    name = 'borrowedmovies-list'


class BorrowedMoviesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BorrowedMovies.objects.all()
    serializer_class = BorrowedMoviesSerializer
    permission_classes = [IsAuthenticated]
    filter_class = BorrowedMoviesFilter
    name = 'borrowedmovies-detail'

class BorrowedSeriesFilter(FilterSet):
    borrowed_date_from = DateTimeFilter(field_name='borrowedDate', lookup_expr='gte')
    borrowed_date_to = DateTimeFilter(field_name='borrowedDate', lookup_expr='lte')

    class Meta:
        model = BorrowedSeries
        fields = ['borrowed_date_from', 'borrowed_date_to']

class BorrowedSeriesList(generics.ListCreateAPIView):
    queryset = BorrowedSeries.objects.all()
    serializer_class = BorrowedSeriesSerializer
    permission_classes = [IsAuthenticated]
    filter_class = BorrowedSeriesFilter
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

class EpisodeDataList(generics.ListCreateAPIView):
    queryset = EpisodeData.objects.all()
    serializer_class = EpisodeDataSerializer
    permission_classes = [IsAuthenticated]
    filter_fields = ['seasonNumber', 'episodeNumber', 'title']
    search_fields = ['seasonNumber', 'episodeNumber', 'title']
    ordering_fields = ['seasonNumber', 'episodeNumber', 'title']
    name = 'episodedata-list'

class EpisodeDataDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EpisodeData.objects.all()
    serializer_class = EpisodeDataSerializer
    permission_classes = [IsAuthenticated]
    name = 'episodedata-detail'

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