from . import views
from django.urls import path


urlpatterns = [
    path('',views.home,name="home"),
    path('parse/',views.parse,name="parse"),
    path('lists/', views.MovieList.as_view(), name='movie_list'),
    
    path('new', views.MovieCreate.as_view(), name='movie_new'),
    path('view/<int:pk>', views.MovieView.as_view(), name='movie_view'),
    path('edit/<int:pk>', views.MovieUpdate.as_view(), name='movie_edit'),
    path('delete/<int:pk>', views.MovieDelete.as_view(), name='movie_delete'),
]
