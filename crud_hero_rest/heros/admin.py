from django.contrib import admin
from heros.models import Hero

class HeroAdmin(admin.ModelAdmin):
    list_display = ('name', 'group')

admin.site.register(Hero, HeroAdmin)