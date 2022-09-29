from django.contrib import admin
from django.urls import path, include, re_path
from . import views
from .models import Music
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'play', views.PlayViewSet, basename='Music')
router.register(r'score', views.UserScoreViewSet, basename='UserScore')

urlpatterns = [
    path('', views.MenuAPI.as_view()),
    re_path(r'^', include(router.urls)),
]
