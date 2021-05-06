from django.urls import path
from .views import user_api_view

urlpatterns = [
    path('usuario/', user_api_view, name="usario_api"),
]