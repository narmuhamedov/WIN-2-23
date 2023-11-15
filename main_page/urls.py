from django.urls import path
from .views import string_post_view, film_detail_view

urlpatterns = [
    path('home_page/', string_post_view),
    path('film_detail/<int:id>/', film_detail_view),
]