from django.urls import path
from . import views
appname = 'movieapp'
# this app name is to prevent the duplication in program. in url we need to define movie.jpeg:demo
# so it will consider from movie.jpeg(app) demo name
urlpatterns = [
     path('', views.demo, name='demo' ),
     path('<int:movie_id>/', views.movie_id, name="movie_id"),
     path('add/', views.add, name="add"),
     path('edit/<int:id>/', views.edit, name="edit"),
     path('delete/<int:id>/', views.delete, name="delete")
]

# <int:movie_id> measn here intiger value we can type which will show in movie_id