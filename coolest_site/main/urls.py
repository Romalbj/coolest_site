from django.urls import path
from . import views

urlpatterns = [
    path('', views.output),
    path('about', views.about)
]
