from django.urls import path
from users.views import user_api_view, user_detail_api_view

urlpatterns = [
    path('usuarios/', user_api_view, name="listar_crear"),
    path('usuarios/<int:pk>/', user_detail_api_view, name="user_detail"),
]