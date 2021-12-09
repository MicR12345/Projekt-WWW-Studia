from rest_framework import serializers
from .models import *
import datetime


class ClientSerializer(serializers.ModelSerializer):
    idClient = serializers.IntegerField()
    owner = serializers.ReadOnlyField(source='owner.username')
    name = serializers.CharField(max_length=45)
    dateOfBirth = serializers.DateField()
    login = serializers.CharField(max_length=45)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

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
        return Client.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.idClient = validated_data.get('idClient', instance.idUser)
        instance.name = validated_data.get('name', instance.name)
        instance.dateOfBirth = validated_data.get('dateOfBirth', instance.dateOfBirth)
        instance.login = validated_data.get('login', instance.login)
        instance.password = validated_data.get('password', instance.password)

    class Meta:
        model = Client
        fields = ['idClient', 'name', 'dateOfBirth','login','owner']


class MovieSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    class Meta:
        model = Movie
        fields = ['idMovie', 'title', 'publicationDate', 'originalLanguage', 'genre', 'director', 'screenwriter',
                  'countryOfOrigin', 'producer','owner']


class SeriesSerializer(serializers.ModelSerializer):

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

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

    class Meta:
        model = Series
        fields = ['idSeries', 'title', 'publicationDate', 'seasonCount', 'totalEpisodeCount','originalLanguage',
        'countryOfOrigin','genre','broadcaster','spinoff','startDate','owner']

class BorrowedMoviesSerializer(serializers.HyperlinkedModelSerializer):
    idMovie = serializers.SlugRelatedField(queryset=Movie.objects.all(), slug_field='title')
    idClient = serializers.SlugRelatedField(queryset=Client.objects.all(), slug_field='login')
    owner = serializers.ReadOnlyField(source='owner.username')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


    class Meta:
        model = BorrowedMovies
        fields = ['idMovie', 'idClient','owner', 'duePayment', 'borrowedDate']


class BorrowedSeriesSerializer(serializers.ModelSerializer):
    idSeries = serializers.SlugRelatedField(queryset=Series.objects.all(), slug_field='title')
    idClient = serializers.SlugRelatedField(queryset=Client.objects.all(), slug_field='login')
    owner = serializers.ReadOnlyField(source='owner.username')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    class Meta:
        model = BorrowedSeries
        fields = ['idSeries', 'idClient','owner', 'duePayment', 'borrowedDate']

class SubtitlesSerializer(serializers.ModelSerializer):
    idMovie = serializers.SlugRelatedField(queryset=Movie.objects.all(), slug_field='title')
    idSeries = serializers.SlugRelatedField(queryset=Series.objects.all(), slug_field='title')
    owner = serializers.ReadOnlyField(source='owner.username')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    class Meta:
        model = Subtitles
        fields = ['idMovie', 'idSeries', 'subtitles','owner']

class EpisodeDataSerializer(serializers.ModelSerializer):
    idSeries = serializers.SlugRelatedField(queryset=Series.objects.all(), slug_field='title')

    class Meta:
        model = EpisodeData
        fields = ['idEpisode', 'idSeries', 'seasonNumber', 'episodeNumber', 'title']
