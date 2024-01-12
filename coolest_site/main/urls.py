from django.urls import path
from . import views

urlpatterns = [
    path('', views.output, name='home'),
    path('about', views.about, name='about'),
    path('works', views.works, name='works')
]
