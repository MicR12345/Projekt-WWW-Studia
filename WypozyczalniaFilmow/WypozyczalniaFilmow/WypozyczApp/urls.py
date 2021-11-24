from django.urls import path

from . import views

urlpatterns = [
    path('user',views.UserList.as_view(),name=views.UserList.name),
    path('user/<int:pk>',views.UserDetail.as_view(),name=views.UserDetail.name),
    path('series',views.SeriesList.as_view(),name=views.SeriesList.name),
    path('series/<int:pk>',views.SeriesDetail.as_view(),name=views.SeriesDetail.name),
    path('movie',views.MovieList.as_view(),name=views.MovieList.name),
    path('movie/<int:pk>',views.MovieDetail.as_view(),name=views.MovieDetail.name),
    path('borrowedmovies',views.BorrowedMoviesList.as_view(),name=views.BorrowedMoviesList.name),
    path('borrowedmovies/<int:pk>',views.BorrowedMoviesDetail.as_view(),name=views.BorrowedMoviesDetail.name),
    path('borrowedseries',views.BorrowedSeriesList.as_view(),name=views.BorrowedSeriesList.name),
    path('borrowedseries/<int:pk>',views.BorrowedSeriesDetail.as_view(),name=views.BorrowedSeriesDetail.name),
    path('subtitles',views.SubtitlesList.as_view(),name=views.SubtitlesList.name),
    path('subtitles/<int:pk>',views.SubtitlesDetail.as_view(),name=views.SubtitlesDetail.name),
    path('episodedata', views.EpisodeDataList.as_view(), name=views.EpisodeDataList.name),
    path('episodedata/<int:pk>', views.EpisodeDataDetail.as_view(), name=views.EpisodeDataDetail.name),
    path('', views.index, name='index'),
]