from django.urls import path
from heros.views import heros_api_view, one_hero_api_view 

urlpatterns = [
    path('heros/', heros_api_view, name="heros"),
    path('heros/<int:pk>/', one_hero_api_view, name="heros"),
]