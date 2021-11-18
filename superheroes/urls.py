
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'superheroes'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:hero_id>/', views.detail, name = 'detail'),
    path('new/', views.create, name = 'create'),
    path('edit/<int:hero_id>/', views.update_hero, name = 'update_hero'),
    path('delete/<int:hero_id>/', views.delete, name = 'delete')] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)