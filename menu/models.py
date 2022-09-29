from django.db import models
from django.contrib.auth.models import User


class Music(models.Model):
    file = models.FileField(upload_to='musics/')
    name = models.CharField(max_length=100)
    path = models.CharField(max_length=300)

    def save(self, *args, **kwargs):
        self.name = str(self.file).split('/')[-1]
        self.path = "C:\\Users\\969\\PycharmProjects\\DOLG\\media\\musics\\" + str(self.name)
        super(Music, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.name)


class UserScore(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
        return str(self.user) + ": " + str(self.score)
