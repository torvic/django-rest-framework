from django.urls import path
from users.views import user_api_view, user_detail_api_view

urlpatterns = [
    path('listar_crear/', user_api_view, name="listar_crear"),
    path('<int:pk>/', user_detail_api_view, name="user_detail"),
]