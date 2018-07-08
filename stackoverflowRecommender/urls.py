from django.conf.urls import url

from . import views

urlpatterns = [
    url('profile', views.loadProfile, name='profile'),
    url('login', views.login , name='index'),
    url('similarQuestions', views.getSimilarQuestions, name='similarQuestions'),
    url('recommendations', views.loadRecommendations, name='recommendations'),

]