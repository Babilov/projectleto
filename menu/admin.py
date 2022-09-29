from django.contrib import admin
from .models import Music, UserScore


class MusicAdmin(admin.ModelAdmin):
    exclude = ('path', 'name', )


admin.site.register(Music, MusicAdmin)
admin.site.register(UserScore)

