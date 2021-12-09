from django.db import models


# Create your models here.


class Client(models.Model):
    idClient = models.AutoField(primary_key=True)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=45)
    dateOfBirth = models.DateField()
    login = models.CharField(max_length=45)


class Movie(models.Model):
    idMovie = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, unique=True)
    publicationDate = models.DateField(blank=True, null=True)
    originalLanguage = models.CharField(max_length=45, blank=True, null=True)
    genre = models.CharField(max_length=45, blank=True, null=True)
    director = models.CharField(max_length=45, blank=True, null=True)
    screenwriter = models.CharField(max_length=45, blank=True, null=True)
    countryOfOrigin = models.CharField(max_length=45, blank=True, null=True)
    producer = models.CharField(max_length=45, blank=True, null=True)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, blank=True, null=True)


class BorrowedMovies(models.Model):
    idMovie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    idClient = models.ForeignKey(Client, on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    duePayment = models.FloatField()
    borrowedDate = models.DateField()


class Series(models.Model):
    idSeries = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, unique=True)
    publicationDate = models.DateField(blank=True, null=True)
    seasonCount = models.IntegerField(blank=True, null=True)
    totalEpisodeCount = models.IntegerField(blank=True, null=True)
    originalLanguage = models.CharField(max_length=45, blank=True, null=True)
    countryOfOrigin = models.CharField(max_length=45, blank=True, null=True)
    genre = models.CharField(max_length=45, blank=True, null=True)
    broadcaster = models.CharField(max_length=45, blank=True, null=True)
    spinoff = models.IntegerField(blank=True, null=True)
    startDate = models.DateField(blank=True, null=True)
    producer = models.CharField(max_length=45, blank=True, null=True)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, blank=True, null=True)


class BorrowedSeries(models.Model):
    idSeries = models.ForeignKey(Series, on_delete=models.CASCADE)
    idClient = models.ForeignKey(Client, on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    duePayment = models.FloatField()
    borrowedDate = models.DateField()


class Subtitles(models.Model):
    idMovie = models.ForeignKey(Movie, on_delete=models.CASCADE, blank=True, null=True)
    idSeries = models.ForeignKey(Series, on_delete=models.CASCADE, blank=True, null=True)
    subtitles = models.TextField()
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, blank=True, null=True)


class EpisodeData(models.Model):
    idEpisode = models.IntegerField(primary_key=True, unique=True)
    idSeries = models.ForeignKey(Series, on_delete=models.CASCADE)
    seasonNumber = models.IntegerField()
    episodeNumber = models.IntegerField()
    title = models.CharField(max_length=200)
