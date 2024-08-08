
from django.urls import path  # type: ignore
from . import views


urlpatterns = [
path('', views.home , name='all_django_01'),
path('about/', views.about, name='about'),
]
