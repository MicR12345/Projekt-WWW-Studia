from rest_framework import serializers
from .models import *
import datetime


class UserSerializer(serializers.ModelSerializer):
    idUser = serializers.IntegerField()
    name = serializers.CharField(max_length=45)
    dateOfBirth = serializers.DateField()
    login = serializers.CharField(max_length=45)
    password = serializers.CharField(max_length=45)
    accessLevel = serializers.IntegerField()

    def validate_dateOfBirth(self,value):
        if value > datetime.date.today():
            raise serializers.ValidationError(
                "Born in the future"
            )
        return value

    def validate_accessLevel(self,value):
        if value<0:
            raise serializers.ValidationError(
                "Access level cant be lower than 0"
            )
        return value

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.idUser = validated_data.get('idUser', instance.idUser)
        instance.name = validated_data.get('name', instance.name)
        instance.dateOfBirth = validated_data.get('dateOfBirth', instance.dateOfBirth)
        instance.login = validated_data.get('login', instance.login)
        instance.password = validated_data.get('password', instance.password)
        instance.accessLevel = validated_data.get('accessLevel', instance.accessLevel)

    class Meta:
        model = User
        fields = ['idUser', 'name', 'dateOfBirth','login', 'password', 'accessLevel']


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['idMovie', 'title', 'publicationDate', 'originalLanguage', 'genre', 'director', 'screenwriter',
                  'countryOfOrigin', 'producer']


class SeriesSerializer(serializers.Serializer):
    idSeries = serializers.IntegerField()
    title = serializers.CharField(max_length=200)
    publicationDate = serializers.DateField()
    seasonCount = serializers.IntegerField()
    totalEpisodeCount = serializers.IntegerField()
    originalLanguage = serializers.CharField(max_length=45)
    countryOfOrigin = serializers.CharField(max_length=45)
    genre = serializers.CharField(max_length=45)
    broadcaster = serializers.CharField(max_length=45)
    spinoff = serializers.IntegerField()
    startDate = serializers.DateField()
    producer = serializers.CharField(max_length=45)

    def validate_title(self, value):
        if value == '':
            raise serializers.ValidationError(
                "Title can't be empty"
            )
        return value

    def validate_publicationDate(self, value):
        if value != '':
            try:
                datetime.date.strftime(value, '%Y.%m.%d')
            except ValueError:
                raise serializers.ValidationError("Incorrect data format, should be YYYY.MM.DD")
        return value

    def create(self, validatedData):
        return Series.objects.create(**validatedData)

    def update(self, instance, validatedData):
        instance.idSeries = validatedData.get('idSeries', instance.idSeries)
        instance.title = validatedData.get('title',instance.title)
        instance.publicationDate = validatedData.get('publicationDate', instance.publicationDate)
        instance.seasonCount = validatedData.get('seasonCount', instance.seasonCount)
        instance.totalEpisodeCount = validatedData.get('totalEpisodeCount', instance.totalEpisodeCount)
        instance.originalLanguage = validatedData.get('originalLanguage', instance.originalLanguage)
        instance.countryOfOrigin = validatedData.get('countryOfOrigin', instance.countryOfOrigin)
        instance.genre = validatedData.get('genre', instance.genre)
        instance.broadcaster = validatedData.get('broadcaster', instance.broadcaster)
        instance.spinoff = validatedData.get('spinoff', instance.spinoff)
        instance.startDate = validatedData.get('startDate', instance.startDate)
        instance.producer = validatedData.get('producer', instance.producer)


class BorrowedMoviesSerializer(serializers.ModelSerializer):
    idMovie = MovieSerializer(read_only=True)
    idUser = UserSerializer(read_only=True)

    class Meta:
        model = BorrowedMovies
        fields = ['idMovie', 'idUser', 'duePayment', 'borrowedDate']


class BorrowedSeriesSerializer(serializers.ModelSerializer):
    idSeries = SeriesSerializer(read_only=True)
    idUser = UserSerializer(read_only=True)

    class Meta:
        model = BorrowedSeries
        fields = ['idSeries', 'idUser', 'duePayment', 'borrowedDate']

class SubtitlesSerializer(serializers.ModelSerializer):
    idMovie = MovieSerializer(read_only=True)
    idSeries = SeriesSerializer(read_only=True)

    class Meta:
        model = Subtitles
        fields = ['idMovie', 'idSeries', 'subtitles']

class EpisodeDataSerializer(serializers.ModelSerializer):
    idSeries = SeriesSerializer(read_only=True)

    class Meta:
        model = Subtitles
        fields = ['idEpisode', 'idSeries', 'seasonNumber', 'episodeNumber', 'title']
