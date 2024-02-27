from django.urls import path
from . import views

urlpatterns = [
    path('', views.output, name='home1'),
    path('home', views.output, name='home'),
    path('about', views.about, name='about'),
    path('works', views.works, name='works'),
    path('beauty', views.beauty, name='beauty')

]
