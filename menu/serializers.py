import random
import time
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Music, UserScore


# class MethodField(serializers.SerializerMethodField):
#     def __init__(self, method_name=None, **kwargs):
#         # use kwargs for our function instead, not the base class
#         super().__init__(method_name)
#         self.func_kwargs = kwargs
#         print(kwargs)
#
#     def to_representation(self, value):
#         method = getattr(self.parent, self.method_name)
#         return method(value, **self.func_kwargs)


class MusicSerializer(serializers.Serializer): # noqa

    first_id = Music.objects.first().id
    last_id = Music.objects.last().id

    random.seed(time.perf_counter())
    ids = random.sample(range(first_id, last_id), 4)

    rand_number_for_answer = ids[0]

    first_wrong = ids[1]

    second_wrong = ids[2]

    third_wrong = ids[3]

    random_track = serializers.SerializerMethodField('get_random_music')
    answers = serializers.SerializerMethodField('get_answers')
    path = serializers.SerializerMethodField('get_path')

    def get_random_music(self, obj): # noqa
        return str(Music.objects.get(pk=self.rand_number_for_answer))

    def get_answers(self, obj): # noqa
        right_answer = Music.objects.get(pk=self.rand_number_for_answer)
        answers = [
                str(Music.objects.get(pk=self.first_wrong)),
                str(Music.objects.get(pk=self.second_wrong)),
                str(Music.objects.get(pk=self.third_wrong)),
                str(right_answer),
        ]

        random.shuffle(answers)
        return answers

    def get_path(self, obj):
        track = Music.objects.get(pk=self.rand_number_for_answer)
        return str(track.path)


class UserScoreSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = UserScore
        fields = ('user', 'score')
