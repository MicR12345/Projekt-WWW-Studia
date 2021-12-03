import datetime

from rest_framework.test import APITestCase, APIClient
from rest_framework.reverse import reverse
from rest_framework import status
from .models import Movie, Series
from .views import MovieList, SeriesList,MovieDetail, SeriesDetail

from django.contrib.auth.models import User

class MovieTests(APITestCase):
    def create_users(self):
        if len(User.objects.all())==0:
            User.objects.create_superuser('admin123', 'admin@admin.com', 'admin123')
        if len(User.objects.all()) == 1:
            User.objects.create_user('test', 'test@test.test', 'test')

    def post_movie_without_login(self, title):
        url = reverse(MovieList.name)
        data = {'title': title}
        response = self.client.post(url, data, format='json')
        return response

    def post_movie(self,title):
        self.create_users()
        client = APIClient()
        client.login(username='admin123', password='admin123')
        url = reverse(MovieList.name)
        data = {'title': title}
        response = client.post(url, data, format='json')
        return response

    def post_movie_as_user(self,title):
        self.create_users()
        client = APIClient()
        client.login(username='test', password='test')
        url = reverse(MovieList.name)
        data = {'title': title}
        response = client.post(url, data, format='json')
        return response

    def get_movies_without_login(self):
        client = APIClient()
        url = reverse(MovieList.name)
        response = client.get(url,format='json')
        return response

    def get_movies_as_user(self):
        self.create_users()
        client = APIClient()
        client.login(username='test', password='test')
        url = reverse(MovieList.name)
        response = client.get(url,format='json')
        return response

    def test_post_movie_without_login(self):
        movie = 'test'
        response_one = self.post_movie_without_login(movie)
        assert response_one.status_code == status.HTTP_403_FORBIDDEN

    def test_post_movie(self):
        movie = 'test'
        response_one = self.post_movie(movie)
        assert response_one.status_code == status.HTTP_201_CREATED

    def test_post_existing_movie_title(self):
        url = reverse(MovieList.name)
        new_movie_title = 'Duplicate Test'
        data = {'title': new_movie_title}
        response_one = self.post_movie(new_movie_title)
        assert response_one.status_code == status.HTTP_201_CREATED
        response_two = self.post_movie(new_movie_title)
        assert response_two.status_code == status.HTTP_400_BAD_REQUEST

    def test_get_movie_as_user(self):
        assert self.get_movies_as_user().status_code == status.HTTP_200_OK

    def test_get_movie_without_login(self):
        assert self.get_movies_without_login().status_code == status.HTTP_200_OK

    def test_post_movie_as_user(self):
        movie = 'test_as_user'
        assert self.post_movie_as_user(movie).status_code == status.HTTP_201_CREATED

    def test_movie_update_title(self):
        title = 'test'
        response = self.post_movie(title)
        url = reverse(MovieDetail.name,kwargs={'pk':response.data['idMovie']})
        new_title = 'test2'
        data = {'title': new_title}
        client = APIClient()
        client.login(username='admin123', password='admin123')
        get_response = client.patch(url,data,format='json')
        assert get_response.status_code == status.HTTP_200_OK
        assert get_response.data['title'] == new_title

    def test_get_movie_title(self):
        title = 'test3'
        response = self.post_movie(title)
        url = reverse(MovieDetail.name, kwargs={'pk': response.data['idMovie']})
        client = APIClient()
        client.login(username='admin123', password='admin123')
        get_response = client.patch(url,format='json')
        assert get_response.status_code == status.HTTP_200_OK
        assert get_response.data['title'] == title

# def test_filter_movie_by_title(self):
#     movie_name_one= 'Test'
class SeriesTest(APITestCase):
    def create_users(self):
        if len(User.objects.all())==0:
            User.objects.create_superuser('admin123', 'admin@admin.com', 'admin123')
        if len(User.objects.all()) == 1:
            User.objects.create_user('test', 'test@test.test', 'test')

    def post_series_without_login(self, title):
        url = reverse(SeriesList.name)
        data = {'title': title}
        response = self.client.post(url, data, format='json')
        return response

    def post_series(self,title):
        self.create_users()
        client = APIClient()
        client.login(username='admin123', password='admin123')
        url = reverse(SeriesList.name)
        data = {'title': title}
        response = client.post(url, data, format='json')
        return response

    def get_series_without_login(self):
        client = APIClient()
        url = reverse(SeriesList.name)
        response = client.get(url,format='json')
        return response

    def get_series_as_user(self):
        self.create_users()
        client = APIClient()
        client.login(username='test', password='test')
        url = reverse(SeriesList.name)
        response = client.get(url,format='json')
        return response

    def test_post_series_without_login(self):
        series = 'test'
        response_one = self.post_series_without_login(series)
        assert response_one.status_code == status.HTTP_403_FORBIDDEN

    def test_post_existing_series_title(self):
        url = reverse(SeriesList.name)
        new_series_title = 'Duplicate Test'
        data = {'title': new_series_title}
        response_one = self.post_series(new_series_title)
        assert response_one.status_code == status.HTTP_201_CREATED
        response_two = self.post_series(new_series_title)
        assert response_two.status_code == status.HTTP_400_BAD_REQUEST

    def test_get_series_as_user(self):
        assert self.get_series_as_user().status_code == status.HTTP_200_OK

    def test_post_series(self):
        series = 'test'
        response_one = self.post_series(series)
        assert response_one.status_code == status.HTTP_201_CREATED

    def test_update_series_title(self):
        title = 'test'
        response = self.post_series(title)
        url = reverse(SeriesDetail.name,kwargs={'pk':response.data['idSeries']})
        updated_series_title = 'BestTest'
        data = {'title': updated_series_title}
        client = APIClient()
        client.login(username='admin123', password='admin123')
        patch_response = client.patch(url, data, format='json')
        assert patch_response.status_code == status.HTTP_200_OK
        assert patch_response.data['title'] == updated_series_title
