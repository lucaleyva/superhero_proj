from django.urls import path
from django.urls.resolvers import URLPattern
from . import views


app_name = 'superheroes'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:hero_id>/', views.detail, name='detail'),
    path('new/', views.create, name='create'),
    path('update_hero/<int:hero_id>/', views.update_hero, name='update_hero'),
    path('delete_hero/<int:hero_id>/', views.delete_hero, name='delete_hero')]