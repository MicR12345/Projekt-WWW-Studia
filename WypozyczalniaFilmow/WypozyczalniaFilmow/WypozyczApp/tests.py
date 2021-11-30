import datetime

from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework.reverse import reverse
from . import views
from .models import User, Movie, BorrowedMovies, Series, BorrowedSeries, Subtitles, EpisodeData
from rest_framework import status
from django.utils.http import urlencode
from django import urls
from django.contrib.auth.models import User


# Create your tests here.
class UserTests(APITestCase):
    def post_user(self,login):
        url = reverse(views.UserList.name)
        data = {'login': login}
        response = self.client.post(url, data, format='json')
        return response

    def test_post_and_get_user(self):
        new_login = 'WAWAWAWAWA'
        response = self.post_user(new_login)
        print(User.objects.count())
        #print("PK {0}".format(User.objects.get().pk))
        assert response.status_code == status.HTTP_201_CREATED
        assert User.objects.count() == 1
        assert User.objects.get().name == new_login

    def post_user_with_future_dateOfBirth(self):
        User.objects.create_superuser('admin', 'admin@admin.com', 'admin123')
        client = APIClient()
        date = datetime.date.today() + datetime.timedelta(days=1)
        name = 'awawawawa'
        login = 'tezd'
        password = 'dddddddd'
        accessLevel = 1
        response = self.create_User(name,date,login,password,accessLevel,client)
        assert response.status_code == status.HTTP_201_CREATED
        assert User.objects.count() == 1
        assert User.objects.get().name == name
        assert User.objects.get().login == login


class MovieTests(APITestCase):
    def post_movie(self, title):
        url = reverse(views.MovieList.name)
        data = {'title': title}
        response = self.client.post(url, data, format='json')
        return response

    def test_post_and_get_movie(self):
        new_movie_title = 'Test'
        response = self.post_movie(new_movie_title)
        print("PK {0}".format(Movie.objects.get().pk))
        assert response.status_code == status.HTTP_201_CREATED
        assert Movie.objects.count() == 1
        assert Movie.objects.get().name == new_movie_title

    def test_post_existing_movie_title(self):
        url = reverse(views.MovieList.name)
        new_movie_title = 'Duplicate Test'
        data = {'title': new_movie_title}
        response_one = self.post_movie(new_movie_title)
        assert response_one.status_code == status.HTTP_201_CREATED
        response_two = self.post_movie(new_movie_title)
        print(response_two)
        assert response_two.status_code == status.HTTP_400_BAD_REQUEST

   # def test_filter_movie_by_title(self):
   #     movie_name_one= 'Test'
