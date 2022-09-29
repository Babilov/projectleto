from django.core import serializers
from django.shortcuts import render
import json
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Music, UserScore
from .serializers import MusicSerializer, UserScoreSerializer


class MenuAPI(APIView):

    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, *args, **kwargs):
        return Response({"play_url": "http://127.0.0.1:8000/play", "score_url": "http://127.0.0.1:8000/score"}, template_name='menu/index.html')


class PlayViewSet(ViewSet):
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]
    template_name = 'menu/game.html'
    def list(self, request): # noqa
        queryset = Music.objects.all()
        serializer_class = MusicSerializer(queryset)

        return render(request, template_name=self.template_name, context={'data': serializer_class.data})


class UserScoreViewSet(ReadOnlyModelViewSet):
    queryset = UserScore.objects.order_by('-score')
    serializer_class = UserScoreSerializer
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]
    template_name = 'menu/score.html'

    def list(self, request, *args, **kwargs):
        return render(request=request, template_name=self.template_name, context={'scores': self.queryset})

