from django.db import models

# Create your models here.


class User(models.Model):
    idUser = models.IntegerField(primary_key=True,unique=True)
    name = models.CharField(max_length=45)
    dateOfBirth = models.DateField()
    login = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    accessLevel = models.IntegerField()


class Movie(models.Model):
    idMovie = models.IntegerField(primary_key=True,unique=True)
    title = models.CharField(max_length=200)
    publicationDate = models.DateField()
    originalLanguage = models.CharField(max_length=45)
    genre = models.CharField(max_length=45)
    director = models.CharField(max_length=45)
    screenwriter = models.CharField(max_length=45)
    countryOfOrigin = models.CharField(max_length=45)
    producer = models.CharField(max_length=45)


class BorrowedMovies(models.Model):
    idMovie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    idUser = models.ForeignKey(User, on_delete=models.CASCADE)
    duePayment = models.FloatField()
    borrowedDate = models.DateField()


class Series(models.Model):
    idSeries = models.IntegerField(primary_key=True, unique=True)
    title = models.CharField(max_lenght=200)
    publicationDate = models.DateField()
    seasonCount = models.IntegeField()
    totalEpisodeCount = models.ItegerField()
    originalLanguage = models.CharField(max_lenght=45)
    countryOfOrigin = models.CharField(max_lenght=45)
    genre = models.CharField(max_lenght=45)
    broadcaster = models.CharField(max_lenght=45)
    spinoff = models.IntegerField()
    startDate = models.DateField()
    producer = models.CharField(max_lenght=45)


class BorrowedMovies(models.Model):
    idSeries = models.ForeignKey(Series, on_delete=models.CASCADE)
    idUser = models.ForeignKey(User, on_delete=models.CASCADE)
    duePayment = models.FloatField()
    borrowedDate = models.DateField()


class Subtitles(models.Model):
    idMovie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    idSeries = models.ForeignKey(Series, on_delete=models.CASCADE)
    subtitles = models.TextField()


class EpisodeData(models.Model):
    idEpisode = models.IntegerField(primary_key=True, unique=True)
    idSeries = models.ForeignKey(Series, on_delete=models.CASCADE)
    seasonNumber = models.IntegerField()
    episodeNumber = models.IntegerField()
    title = models.CharField(max_lenght=200)